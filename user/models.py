from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # 自增主键
    username = models.CharField(max_length=30)  # 字符串类型，最大长度为30
    password = models.CharField(max_length=30)  # 字符串类型，最大长度为30
    email = models.EmailField(max_length=30)  # 字符串类型，最大长度为30

    def __str__(self):  # 在admin站点中显示的名称
        return self.username

    class Meta:  # 元数据
        db_table = "user"  # 指定表名
        verbose_name = "用户"  # 指定在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
