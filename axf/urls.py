from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$', views.home, name='index'),  # 首页
    url(r'^home/$', views.home, name='home'),   # 首页
    url(r'^market/(\d+)/(\d+)/$', views.market, name='market'), # 闪购超市
    url(r'^cart/$', views.cart, name='cart'),   # 购物车
    url(r'^mine/$', views.mine, name='mine'),   # 我的
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.login, name="login"),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^chackAccount/$',views.chackAccount,name='chackAccount'),
    url(r'^chacktel/$',views.chacktel,name="chacktel"),
    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^subcart/$',views.subcart,name='subcart'),
    url(r'^change/$',views.change,name='change'),
    url(r'^changeall/$',views.changeall,name='changeall'),
    url(r'^order/$',views.order,name='order'),
    url(r'^orderdetail/(\d+)/$',views.orderdetail,name='orderdetail'),
    url(r'^notify/$',views.notify,name='notify'),
    url(r'^result/$',views.result,name='result'),
    url(r'^pay/$',views.pay,name='pay'),

]