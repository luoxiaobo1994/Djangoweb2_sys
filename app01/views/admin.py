# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/2/22 13:57

from django.shortcuts import render, redirect
from app01.models import Admin
from app01.utils.pagination import Pagination
from app01.utils.form import AdminModelForm
from app01.models import Admin


def admin_list(request):
    """管理员列表"""
    data_dict = {}
    search_data = request.GET.get('q', '')  # 拿到q携带的参数.
    if search_data:
        data_dict['username__contains'] = search_data  # Django的搜索方式
    queryset = Admin.objects.filter(**data_dict)  # 条件查询
    page_object = Pagination(request, queryset)  # 分页组件
    context = {
        'search_data': search_data,  # 这里是传给前端显示的参数,不是搜索参数.
        'queryset': queryset,
        'page_string': page_object.html()
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """ 添加管理员 """
    title = '新建管理员'  # 页面组件的标题
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {'title': title, 'form': form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'title': title, 'form': form})


def admin_edit(request, nid):
    """ 管理员编辑 """
    title = '编辑管理员'
    row_object = Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/admin/list/")
    form = AdminModelForm()
    return render(request, 'change.html', {'title': title, 'form': form})


def admin_delete(request, nid):
    """ 删除管理员 """
