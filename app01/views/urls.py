# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/7/6 14:26
# Desc:

from django.urls import path
from app01 import views_api

urlpatterns = [
    # 已经实现接口获取，如何获取实际数据呢？
    path('getuser', views_api.get_user),  # 完整请求网址：http://127.0.0.1:8000/app01/getuser
    path('adduser', views_api.add_user),  # 完整请求网址：http://127.0.0.1:8000/app01/adduser
    path('deluser', views_api.del_user),  # 完整请求网址：http://127.0.0.1:8000/app01/deluser
    path('edituser/<int:nid>/', views_api.edit_user),  # 完整请求网址：http://127.0.0.1:8000/app01/edituser
    path('gettoken', views_api.user_token)

]
