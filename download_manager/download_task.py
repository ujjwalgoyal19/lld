import threading
from ast import List

import requests
from download_listener import DownloadListener
from download_part import DownloadPart
from enums import DownloadState


class DownloadTask:
    __total_size: int
    __parts: List[DownloadPart]
    __progress: List[int]

    def __init__(self, url, file_path, thread_count=4):
        self.url = url
        self.file_path = file_path
        self.thread_count = thread_count
        self.state = DownloadState.READY
        self.__pause_event = threading.Event()
        self.__pause_event.set()
        self.__listeners = []
        self.__lock = threading.Lock()

    def add_listener(self, listener: DownloadListener):
        self.__listeners.append(listener)

    def _notify_progress(self):
        percent = (self.__progress[0] / self.__total_size) * 100
        for l in self.__listeners:
            l.on_progress(self.url, percent)

    def _notify_complete(self):
        for l in self.__listeners:
            l.on_complete(self.url, self.file_path)

    def _notify_error(self, error):
        for l in self.__listeners:
            l.on_error(self.url, error)

    def pause(self):
        with self.__lock:
            if self.state == DownloadState.DOWNLOADING:
                self.state = DownloadState.PAUSED
                self.__pause_event.clear()

    def resume(self):
        with self.__lock:
            if self.state == DownloadState.PAUSED:
                self.state = DownloadState.DOWNLOADING
                self.__pause_event.set()

                for part in self.__parts:
                    if not part.is_alive():
                        part.start()

    def run(self):
        try:
            head = requests.head(self.url)
            self.__total_size = int(head.headers.get("Content-length", 0))

            with open(self.file_path, "wb") as f:
                f.truncate(self.__total_size)

            part_size = self.__total_size // self.thread_count
            self.__progress = [0]
            self.__parts = []

            self.state = DownloadState.DOWNLOADING
            for i in range(self.thread_count):
                start = part_size * i
                end = (
                    (self.__total_size - 1)
                    if i == self.thread_count - 1
                    else (start + part_size - 1)
                )
                part = DownloadPart(
                    self.url,
                    self.file_path,
                    start,
                    end,
                    self.__pause_event,
                    self.__progress,
                    self.__total_size,
                )
                self.__parts.append(part)
                part.start()

            for part in self.__parts:
                part.join()

            if self.__progress[0] == self.__total_size:
                self.state = DownloadState.COMPLETED
                self._notify_complete()
            else:
                raise RuntimeError("Incomplete Download")
        except Exception as e:
            self.state = DownloadState.FAILED
            self._notify_error(e)
