from django.db import models

# Create your models here.


class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=60)
    trackid = models.CharField(max_length=10)

    class Meta():
        abstract = True


class Wheel(Base):
    class Meta():
        db_table = "axf_wheel"


class Nav(Base):
    class Meta():
        db_table = "axf_nav"

class Mustbuy(Base):
    class Meta():
        db_table = "axf_mustbuy"

class Shop(Base):
    class Meta():
        db_table ="axf_shop"


class Mainshow(Base):

    categoryid = models.CharField(max_length=80)
    brandname = models.CharField(max_length=80)
    img1 = models.CharField(max_length=80)
    childcid1 = models.CharField(max_length=80)
    productid1 = models.CharField(max_length=80)
    longname1 = models.CharField(max_length=80)
    price1 = models.CharField(max_length=80)
    marketprice1 = models.CharField(max_length=80)
    img2 = models.CharField(max_length=80)
    childcid2 = models.CharField(max_length=80)
    productid2 = models.CharField(max_length=80)
    longname2 = models.CharField(max_length=80)
    price2 = models.CharField(max_length=80)
    marketprice2 = models.CharField(max_length=80)
    img3 = models.CharField(max_length=80)
    childcid3 = models.CharField(max_length=80)
    productid3 = models.CharField(max_length=80)
    longname3 = models.CharField(max_length=80)
    price3 = models.CharField(max_length=80)
    marketprice3 = models.CharField(max_length=80)



    class Meta():
        db_table = "axf_mainshow"


# typeid,typename,childtypenames,typesort
class Foodtype(models.Model):
    typeid = models.CharField(max_length=80)
    typename = models.CharField(max_length=80)
    childtypenames = models.CharField(max_length=80)
    typesort = models.CharField(max_length=80)
    class Meta():
        db_table = "axf_foodtypes"
# ,,,,
# ,,,,,,
# ,,,,
# "50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4
class Goods(models.Model):

    productid = models.CharField(max_length=20)  # 商品ID
    productimg = models.CharField(max_length=100)# 商品图片
    productname = models.CharField(max_length=50)# 商品名字
    productlongname = models.CharField(max_length=100) # 商品长名字
    isxf = models.BooleanField(default=0)  # 精选
    pmdesc = models.BooleanField(default=0) # 买一送一

    specifics = models.CharField(max_length=100) # 规格参数
    price = models.IntegerField() # 价格
    marketprice = models.DecimalField(max_digits=7,decimal_places=2) # 市场价格
    categoryid = models.IntegerField() # 商品分类ID
    childcid = models.IntegerField() # 子分类ID
    childcidname = models.CharField(max_length=100) # 子分类名称
    dealerid = models.CharField(max_length=20)  # 详情ID
    storenums = models.CharField(max_length=20) # 库存
    productnum = models.CharField(max_length=20) # 销量

    class Meta():
        db_table = "axf_goods"


class User(models.Model):

    username = models.CharField(max_length=20)
    account = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=20,unique=True)
    headimg = models.CharField(max_length=30)
    token = models.CharField(max_length=256)
    addr = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)

    class Meta():
        db_table = " axf_user"

class Cart(models.Model):

    user = models.ForeignKey(User)
    goodsid = models.ForeignKey(Goods)
    number = models.IntegerField()
    isselect = models.BooleanField(default=False)

    class Meta():
        db_table = 'axf_cart'