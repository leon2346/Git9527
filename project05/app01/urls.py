from django.conf.urls import url

from app01 import views

urlpatterns = [
    # 进入首页
    url(r'^index/$', views.index),
    # 进入静态文件演示页面
    url(r'^show_static/$', views.show_static),
    # 进入上传图片界面
    url(r'^show_upload_image/$', views.show_upload_image),
    # 处理上传操作
    url(r'^do_upload/$', views.do_upload),
    # 显示上传图片
    url(r'^show_images/$', views.show_images),
    # 显示上传图片
    url(r'^show_page/$', views.show_page),
    # 显示区域案例界面
    url(r'^show_area/$', views.show_area),


]
