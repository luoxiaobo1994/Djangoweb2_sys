# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/2/21 22:45

from django import forms


class BootStrap():
    """ 样式父类,后面创建新样式基础类时,直接继承这个即可 """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环modelform中的所有字段,给每个字段的插件设置样式
        for name, field in self.fields.items():
            # 字段中有属性的,保留原有属性,没有的才新增
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    # 给ModelForm使用的，已经继承了BootStrap基础类，只是把ModelForm加上。
    pass


class BootStrapForm(BootStrap, forms.Form):
    # 同上。
    pass
