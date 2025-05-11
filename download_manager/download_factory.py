from download_task import DownloadTask


class DownloadFactory:
    @staticmethod
    def create_download_task(url, path, threads=4):
        return DownloadTask(url, path, threads)
