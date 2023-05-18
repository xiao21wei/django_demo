from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import User


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        # 获取前端传递的数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # 查询数据库
        user = User.objects.filter(username=username).first()
        if user:
            # 用户已存在
            return JsonResponse({"code": 400, "msg": "用户名已存在", "data": None})
        # 将数据保存到数据库中
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.save()
        # 返回响应
        return JsonResponse({"code": 200, "msg": "用户注册成功", "data": None})
    else:
        return JsonResponse({"code": 400, "msg": "请求方式错误", "data": None})


@csrf_exempt
def login(request):
    if request.method == "POST":
        # 获取前端传递的数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 查询数据库
        user = User.objects.filter(username=username).first()
        if user and user.password == password:
            # 将用户信息保存到session中
            request.session["username"] = user.username
            # 登录成功
            return JsonResponse({"code": 200, "msg": "用户登录成功", "data": None})
        elif user and user.password != password:
            # 密码错误
            return JsonResponse({"code": 400, "msg": "密码错误", "data": None})
        else:
            # 用户不存在
            return JsonResponse({"code": 400, "msg": "用户不存在", "data": None})
    else:
        return JsonResponse({"code": 400, "msg": "请求方式错误", "data": None})


@csrf_exempt
def update(request):
    if request.method == "POST":
        # 获取前端传递的数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # 查询数据库
        user = User.objects.filter(username=username).first()
        if user:
            # 更新数据
            user.username = username
            user.password = password
            user.email = email
            user.save()
            # 返回响应
            return JsonResponse({"code": 200, "msg": "用户信息更新成功", "data": None})
        else:
            # 用户不存在
            return JsonResponse({"code": 400, "msg": "用户不存在", "data": None})
    else:
        return JsonResponse({"code": 400, "msg": "请求方式错误", "data": None})


@csrf_exempt
def logout(request):
    if request.method == "POST":
        # 获取前端传递的数据
        username = request.POST.get("username")
        # 查询数据库
        user = User.objects.filter(username=username).first()
        if user:
            # 删除session中的数据
            del request.session["username"]
            # 返回响应
            return JsonResponse({"code": 200, "msg": "用户退出成功", "data": None})
        else:
            # 用户不存在
            return JsonResponse({"code": 400, "msg": "用户不存在", "data": None})
    else:
        return JsonResponse({"code": 400, "msg": "请求方式错误", "data": None})


@csrf_exempt
def get_user(request):
    if request.method == "POST":
        # 获取前端传递的数据
        username = request.POST.get("username")
        # 查询数据库
        user = User.objects.filter(username=username).first()
        if user:
            # 返回响应
            return JsonResponse({"code": 200, "msg": "获取用户信息成功", "data": {"username": user.username, "password": user.password, "email": user.email}})
        else:
            # 用户不存在
            return JsonResponse({"code": 400, "msg": "用户不存在", "data": None})
    else:
        return JsonResponse({"code": 400, "msg": "请求方式错误", "data": None})
