from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods


def home(request):  # 首页
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shophead = Shop.objects.filter(pk=1).first()
    shoptab = Shop.objects.filter(pk__gt=1,pk__lte=3)
    shopclass = Shop.objects.filter(pk__gt=3,pk__lte=7)
    shopcommends = Shop.objects.filter(pk__gt=7)
    mainshow = Mainshow.objects.all().first()
    data = {
        "wheels": wheels,
        "navs": navs,
        "mustbuys":mustbuys,
        "shophead":shophead,
        "shoptab":shoptab,
        "shopclass":shopclass,
        "shopcommends":shopcommends,
        "mainshow":mainshow

    }
    return render(request, 'home/home.html',context=data)


def market(request, childcid, sortid):    # 闪购超市
    sort_list = ["id", "-productnum", "price", "-price"]
    foodtypes = Foodtype.objects.all()
    typeIndex = request.COOKIES.get("typeIndex",0)
    typeid = Foodtype.objects.filter(pk=int(typeIndex)+1).first().typeid
    if childcid=="0":
        goods = Goods.objects.filter(categoryid=int(typeid)).order_by(sort_list[int(sortid)])
    else:
        goods = Goods.objects.filter(categoryid=int(typeid),childcid=int(childcid)).order_by(sort_list[int(sortid)])
    childtypenames = Foodtype.objects.filter(pk=int(typeIndex)+1).first().childtypenames
    childcidList =[]

    for item in childtypenames.split("#"):
            arr=item.split(":")
            dir={
                'childname':arr[0],
                'childid':arr[1],
            }
            childcidList.append(dir)
    data ={
        "foodtypes":foodtypes,
        "goods":goods,
        'childcidList':childcidList,
        'childcid':childcid,
        'sortid':sortid,
    }
    return render(request, 'market/market.html',context=data)


def cart(request):  # 购物车
    return render(request, 'cart/cart.html')


def mine(request):  # 我的
    return render(request, 'mine/mine.html')