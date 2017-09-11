from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


# USER_DICT = {
#     'k1':'root1',
#     'k2':'root2',
#     'k3':'root3',
#     'k4':'root4',
# }

USER_DICT = {
    '1': {'name': 'root1', 'email': 'root1@live.com'},
    '2': {'name': 'root2', 'email': 'root2@live.com'},
    '3': {'name': 'root3', 'email': 'root3@live.com'},
    '4': {'name': 'root4', 'email': 'root4@live.com'},
    '5': {'name': 'root5', 'email': 'root5@live.com'},
}

def index(request):
    return render(request, 'index.html', {'user_dict':USER_DICT})

# def detail(request):
#     nid = request.GET.get('nid')
#     detail_info = USER_DICT[nid]
#     return render(request,'detail.html',{'detail_info':detail_info})

def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request,'user_info.html',{'user_list':user_list,'group_list':group_list})
    elif request.method =='POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        gid = request.POST.get('group_id')
        models.UserInfo.objects.create(username=u,password=p,user_group_id=gid)
        return redirect('/cmdb/user_info')


def user_group(request):
    if request.method == 'GET':
        group_list = models.UserGroup.objects.all()
        return render(request,'user_group.html',{'group_list':group_list})
    elif request.method =='POST':
        cap = request.POST.get('group')
        models.UserGroup.objects.create(caption=cap)
        return redirect('/cmdb/user_group')


def group_detail(request,nid):
    obj = models.UserGroup.objects.filter(uid=nid).first()
    return render(request,'group_detail.html',{'obj':obj})


def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request,'user_detail.html',{'obj':obj})

def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info')

def group_del(request,nid):
    models.UserGroup.objects.filter(uid=nid).delete()
    return redirect('/cmdb/user_group')


def user_edit(request,nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        obj = models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/user_info')

def detail(request,nid):
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})

from app01 import models

def orm(request):

    #创建数据
    models.UserInfo.objects.create(username='chris',password=123)

    # 查询
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root',password=123)
    # print(result)
    # for row in result:
    #     print(row.id,row.username,row.password)

    # 删除
    # models.UserInfo.objects.filter(id=4).delete()

    # 更新
    # models.UserInfo.objects.all().update(password=66666)

    return HttpResponse('orm')


from django.views import View
class Home(View):

    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Home, self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method)
        return render(request,'home.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if obj:
            return redirect('/cmdb/index')
        else:
            return render(request, 'login.html')

        # radio
        # v = request.POST.get('gender')
        # print(v)
        # v = request.POST.getlist('favor')
        # print(v)
        # v = request.POST.get('fafafa')
        # print(v)
        # obj = request.FILES.get('fafafa')
        # print(obj,type(obj),obj.name)
        # print('1:',obj.chunks,type(obj.chunks),'2:',obj.chunks(),type(obj.chunks()),)
        # file_path = 'upload/' + obj.name
        # f = open(file_path,'wb')
        # for i in obj.chunks():
        #     f.write(i)
        #     f.close()
        # return render(request, 'login.html')
    else:
        # PUT,DELETE,HEAD,OPTION...
        return redirect('/index')
