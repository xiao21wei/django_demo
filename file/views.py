import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        file_name = file.name
        file_type = file_name.split(".")[-1]
        if file_type in ["jpg", "png"]:
            if file_name in os.listdir("static/img"):
                file_name = file_name.split(".")[0] + "1." + file_type
            file_path = "static/img/" + file_name
        elif file_type in ["mp4", "avi"]:
            if file_name in os.listdir("static/video"):
                file_name = file_name.split(".")[0] + "1." + file_type
            file_path = "static/video/" + file_name
        elif file_type in ["mp3", "wav"]:
            if file_name in os.listdir("static/audio"):
                file_name = file_name.split(".")[0] + "1." + file_type
            file_path = "static/audio/" + file_name
        else:
            if file_name in os.listdir("static/file"):
                file_name = file_name.split(".")[0] + "1." + file_type
            file_path = "static/file/" + file_name
        with open(file_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
        return JsonResponse({"code": 200, "msg": "上传成功", "data": {"file_path": file_path}})
