from rest_framework.decorators import api_view
from rest_framework.response import Response
from fs_mng import helper
from fs_mng.config import Config


@api_view()
def get_files_info(request):
    files_info = helper.get_dir_files(Config.BASE_URL)
    return Response(files_info)
