from django.db import models


# Create your models here.

class Department(models.Model):
    # 部门表,只存部门名称
    title = models.CharField(max_length=32, verbose_name="标题")


class UserInfo(models.Model):
    # 员工表,员工信息
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_length=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    # 部门ID是有约束的数据,来自另外一张表的主键.   因为是外键,虽然列名叫depart.但是Django会自动处理为depart_id
    # -to=与哪张表关联. -to_fields=要关联的字段
    # on_delete 级联删除,部门id被删除的情况下,把这个用户也干掉.
    # 也可以,允许置空,设置默认值为空,删除部门ID时,保留该用户.
    # depart = models.ForeignKey(to="Department",to_field="id",null=True,on_delete=models.SET_NULL)  # 可为空方式.
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)