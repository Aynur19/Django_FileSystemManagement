from datetime import datetime


class FileInfoList:
    data = []

    def __init__(self, data):
        self.data = data


class FileInfo:
    name = ''
    type = ''
    time = datetime.now()

    def __init__(self, name: str, type: str, time: datetime):
        self.name = name
        self.type = type
        self.time = time or datetime.now()

    def __str__(self):
        return self.name



