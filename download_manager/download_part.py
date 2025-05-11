import threading
from dataclasses import dataclass

import requests


@dataclass
class DownloadPart(threading.Thread):
    url: str
    path: str
    start: int
    end: int
    pause_event: any
    progress: int
    total_size: int

    def run(self):
        headers = {"Range": f"bytes={self.start}-{self.end}"}
        try:
            resp = requests.get(url=self.url, headers=headers, stream=True)
            resp.raise_for_status()
            with open(self.path, "r+b") as f:
                f.seek(self.start)
                for chunk in resp.iter_content(chunk_size=4096):
                    self.pause_event.wait()
                    f.write(chunk)
                    self.progress[0] += len(chunk)
        except Exception as e:
            raise e
