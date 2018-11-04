import hashlib
import os
import random
import time
import uuid

from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from Python1809AXF import settings
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods, User


def home(request):  # 首页
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shophead = Shop.objects.filter(pk=1).first()
    shoptab = Shop.objects.filter(pk__gt=1, pk__lte=3)
    shopclass = Shop.objects.filter(pk__gt=3, pk__lte=7)
    shopcommends = Shop.objects.filter(pk__gt=7)
    mainshow = Mainshow.objects.all().first()
    data = {
        "wheels": wheels,
        "navs": navs,
        "mustbuys": mustbuys,
        "shophead": shophead,
        "shoptab": shoptab,
        "shopclass": shopclass,
        "shopcommends": shopcommends,
        "mainshow": mainshow

    }
    return render(request, 'home/home.html', context=data)


def market(request, childcid, sortid):  # 闪购超市
    sort_list = ["id", "-productnum", "price", "-price"]
    foodtypes = Foodtype.objects.all()
    typeIndex = request.COOKIES.get("typeIndex", 0)
    typeid = Foodtype.objects.filter(pk=int(typeIndex) + 1).first().typeid
    if childcid == "0":
        goods = Goods.objects.filter(categoryid=int(typeid)).order_by(sort_list[int(sortid)])
    else:
        goods = Goods.objects.filter(categoryid=int(typeid), childcid=int(childcid)).order_by(sort_list[int(sortid)])
    childtypenames = Foodtype.objects.filter(pk=int(typeIndex) + 1).first().childtypenames
    childcidList = []

    for item in childtypenames.split("#"):
        arr = item.split(":")
        dir = {
            'childname': arr[0],
            'childid': arr[1],
        }
        childcidList.append(dir)
    data = {
        "foodtypes": foodtypes,
        "goods": goods,
        'childcidList': childcidList,
        'childcid': childcid,
        'sortid': sortid,
    }
    return render(request, 'market/market.html', context=data)


def cart(request):  # 购物车
    return render(request, 'cart/cart.html')


def mine(request):  # 我的
    token = request.COOKIES.get('token')
    user_list = User.objects.filter(token=token)
    if user_list.exists():
        user = user_list.first()
        username = user.username
        headimg = user.headimg
        data = {
            "username": username,
            "headimg": headimg,
        }
        print(headimg)
        return render(request, 'mine/mine.html', context=data)

    else:
        data = {
            "register": True
        }
        return render(request, 'mine/mine.html', context=data)


def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# 注册
def register(request):
    if request.method == "GET":
        return render(request, 'mine/register.html')
    elif request.method == "POST":
        account = request.POST.get("account")
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassowrd = request.POST.get("repassword")
        tel = request.POST.get("tel")
        addr = request.POST.get("addr")
        file = request.FILES.get('headimg')
        user_list = User.objects.filter(Q(account=account), Q(tel=tel))
        if user_list.exists() or password != repassowrd:
            data = {
                "check": "用户名已存在/密码输入错误"
            }
            return render(request, 'mine/register.html', context=data)
        else:
            # print(account,username, password, addr, file.name)
            filename = str(random.randrange(1, 100)) + '-' + file.name
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            with open(filepath, 'wb') as fb:
                for item in file.chunks():
                    fb.write(item)
            password = generate_password(password)
            user = User()
            user.username = username
            user.password = password
            user.account = account
            user.addr = addr
            user.headimg = 'headimg/' + filename
            user.tel = tel
            user.token = uuid.uuid3(uuid.uuid4(), username)
            response = redirect("axf:mine")
            response.set_cookie('token', user.token)
            user.save()
            return response


def login(request):
    if request.method == "GET":
        return render(request, 'mine/login.html')
    elif request.method == "POST":
        account = request.POST.get("account")
        password = request.POST.get('password')
        user_list = User.objects.filter(account=account)
        if user_list.exists():
            user = user_list.first()
            password = generate_password(password)
            if password == user.password:
                response = redirect("axf:mine")
                response.set_cookie('token',user.token)
                return response
            else:
                data = {
                    "check":"密码错误"
                }
                return render(request,'mine/login.html',context=data)
        else:
            data = {
                "check": "用户不存在"
            }
            return render(request,'mine/login.html',context=data)
    return render(request, 'mine/mine.html')


def logout(request):
    response = redirect('axf:mine')
    response.delete_cookie('token')
    return response