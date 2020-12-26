from django.shortcuts import render, HttpResponse


# Create your views here.
# todo 完成！ 2020/12/24 明天的任务是 1、把templates文件夹\static以及settings的设置搞清楚 2、url的配置搞清楚 3、 写controller的views

def index(request):
    return HttpResponse("登录首页.")

# todo 在这里登录成功应该跳转到管理员控制台首页或者用户首页
