from django.shortcuts import render, HttpResponse, redirect, reverse
from login import models
from django.contrib.auth.decorators import login_required
from django.db.models.query import EmptyQuerySet
from django.contrib import auth
# Create your views here.
# todo 完成！ 2020/12/24 明天的任务是 1、把templates文件夹\static以及settings的设置搞清楚 2、url的配置搞清楚 3、 写controller的views

# @login_required
# def index(request):
#     return render(request, 'login/login.html')

def index(request):
    if request.method == 'POST':
        # 处理POST请求的逻辑
        # 获取用户提交的用户名与密码
        # request.POST.get('user')
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        DB_user = models.UserInfo.objects.filter(UserAccount=user)  # 数据库账户

        # 进行校验
        if DB_user.count() == 0:
            return HttpResponse('用户名有误！')

        DB_pwd = models.UserInfo.objects.filter(UserAccount=user)[0].UserPwd  # 获取数据库密码

        if DB_pwd != pwd:
            return HttpResponse('密码有误')
        elif DB_pwd == pwd: # 校验成功
            return redirect('controller:index')
    return render(request, 'login/login.html')
        # 校验成功：登陆成功
        # 校验失败：返回登录页面

    # if request.method == 'GET':
    #     return render(request, 'login/login.html')
    # else:
    #     # 处理POST请求的逻辑
    #     # 获取用户提交的用户名与密码
    #     # request.POST.get('user')
    #     user = request.POST.get('user')
    #     pwd = request.POST.get('pwd')
    #     DB_user = models.UserInfo.objects.filter(UserAccount=user) # 数据库账户
    #
    #     # 进行校验
    #     if DB_user.count() == 0:
    #         return HttpResponse('用户名有误！')
    #
    #     DB_pwd = models.UserInfo.objects.filter(UserAccount=user)[0].UserPwd  # 获取数据库密码
    #
    #     if DB_pwd != pwd:
    #         return HttpResponse('密码有误')
    #     elif DB_pwd == pwd:
    #         return HttpResponse('登陆成功')
    #         # return render(request, 'login/login.html')
    #     # 校验成功：登陆成功
    #     # 校验失败：返回登录页面







# todo 在这里登录成功应该跳转到管理员控制台首页或者用户首页
