import mimetypes
import os
from datetime import datetime
from os import listdir
from os.path import isfile, join

from fs_mng.models import FileInfo, FileInfoList
from fs_mng.serializers import FileInfoSerializer, FileInfoListSerializer


def get_dir_files(catalog):
    files_info = []
    files = [f for f in listdir(catalog) if isfile(join(catalog, f))]

    for f in files:
        file_path = join(catalog, f)
        file_mime_type = mimetypes.guess_type(file_path, False)[0]
        file_time = datetime.fromtimestamp(os.path.getctime(file_path))
        f1 = FileInfo(f, file_mime_type, file_time)
        file_info = FileInfoSerializer(f1)
        files_info.append(file_info.data)

    files_info_list = FileInfoListSerializer(FileInfoList(files_info))

    return files_info_list.data
