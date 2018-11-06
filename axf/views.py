import hashlib
import os
import random
import time
import uuid

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Python1809AXF import settings
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods, User, Cart


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
    # data = {
    #     "foodtypes": foodtypes,
    #     "goods": goods,
    #     'childcidList': childcidList,
    #     'childcid': childcid,
    #     'sortid': sortid,
    # }
    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)

    data = {
        "foodtypes": foodtypes,
        "goods": goods,
        'childcidList': childcidList,
        'childcid': childcid,
        'sortid': sortid,
        'carts':carts,
    }
    print(carts)
    return render(request, 'market/market.html', context=data)


def cart(request):  # 购物车
    token = request.session.get('token')
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)
        return render(request,'cart/cart.html', context={'carts':carts})
    else:
        return render(request, 'mine/mine.html')


def mine(request):  # 我的
    token = request.session.get('token')
    if token:
        user = User.objects.get(token=token)
        data = {
            'rank': user.rank,
            'username': user.username,
            'headimg': user.headimg,
        }
        return render(request, 'mine/mine.html', context=data)
    else:
        data = {
            'rank': '无',
            'username': '',
            'headimg': '',
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
        user = User()
        user.username = request.POST.get("username")
        user.password = generate_password(request.POST.get("password"))
        user.account = request.POST.get("account")
        file = request.FILES.get('headimg')
        filename = str(user.username) + ".png"
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        with open(filepath, 'wb') as fb:
            for item in file.chunks():
                fb.write(item)
        user.addr = request.POST.get("addr")
        user.headimg = 'headimg/' + filename
        user.tel = request.POST.get("tel")
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        user.save()
        request.session['token'] = user.token
        return redirect("axf:mine")


def login(request):
    if request.method == "GET":
        return render(request, 'mine/login.html')
    elif request.method == "POST":
        account = request.POST.get("account")
        password = request.POST.get('password')
        print(account)
        try:
            user = User.objects.get(account=account)
            if user.password == generate_password(password):
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                request.session['token'] = user.token
                user.save()
                return redirect('axf:mine')
            else:
                return render(request,'mine/login.html',context={'passwordErr':"密码错误!"})
        except:
            return render(request,'mine/login.html',context={'accountErr':'账号不存在'})

    #     user_list = User.objects.filter(account=account)
    #     if user_list.exists():
    #         user = user_list.first()
    #         password = generate_password(password)
    #         if password == user.password:
    #             response = redirect("axf:mine")
    #             response.set_cookie('token',user.token)
    #             return response
    #         else:
    #             data = {
    #                 "check":"密码错误"
    #             }
    #             return render(request,'mine/login.html',context=data)
    #     else:
    #         data = {
    #             "check": "用户不存在"
    #         }
    #         return render(request,'mine/login.html',context=data)
    # return render(request, 'mine/mine.html')


def logout(request):
    request.session.flush()
    return render(request, 'mine/mine.html')


def chackAccount(request):
    account = request.GET.get("account")
    JsonData = {
        'content': "账号可以使用",
        'status': 1
    }
    try:
        user = User.objects.get(account=account)
        JsonData = {
            'content': "账号已存在!",
            'status': -1
        }
        return JsonResponse(JsonData)
    except:
        return JsonResponse(JsonData)


def chacktel(request):
    tel = request.GET.get('tel')
    JsonData = {
        'content': "手机号可以使用",
        'status': 1
    }
    try:
        user = User.objects.get(tel=tel)
        JsonData = {
            'content': "手机号已存在!",
            'status': -1
        }
        return JsonResponse(JsonData)
    except:
        return JsonResponse(JsonData)


def addcart(request):
    token = request.session.get('token')
    goodsid = request.GET.get('goodsid')
    if token:
        user = User.objects.get(token=token)
        goodsid = Goods.objects.get(pk=goodsid)
        user_cart = Cart.objects.filter(user=user).filter(goodsid=goodsid)
        if user_cart.exists():
            cart = user_cart.first()
            cart.number = cart.number + 1
            cart.save()
            return JsonResponse({'status':1,'number':cart.number})
        else:
            cart = Cart()
            cart.user = user
            cart.goodsid = goodsid
            cart.number = 1
            cart.save()
            return JsonResponse({'status':1,'number':cart.number})

    else:
        return JsonResponse({"status":-1,'number':0})


def subcart(request):


    goodsid = request.GET.get('goodsid')
    token = request.session.get('token')
    user = User.objects.get(token=token)
    cart = Cart.objects.filter(user=user).filter(goodsid=goodsid).first()
    cart.number = cart.number - 1
    cart.save()
    return JsonResponse({'status':1,"number":cart.number})