from concurrent.futures import ThreadPoolExecutor
from turtle import listen
from typing import List

from download_factory import DownloadFactory
from download_listener import DownloadListener
from download_task import DownloadTask
from singleton import SingletonMeta


class DownloadManager(meta=SingletonMeta):
    def __init__(self, max_workers=5):
        self.__executor = ThreadPoolExecutor(max_workers=max_workers)
        self._tasks = {}

    def add_download(self, url, path, threads=4, listener: DownloadListener = None):
        task = DownloadFactory.create_download_task(url, path, threads)
        if listener:
            task.add_listener(listener=listener)

        self._tasks[url] = task
        self.__executor.submit(task.run)

    def pause_download(self, url):
        task = self._tasks.get(url)
        if task:
            task.pause()

    def resume_download(self, url):
        task = self._tasks.get(url)
        if task:
            task.resume()

    def shutdown(self):
        self.__executor.shutdown(wait=True)
