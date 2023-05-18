from django.db import models


# Create your models here.
class File(models.Model):
    file_id = models.AutoField(primary_key=True)  # 自增主键
    file_name = models.CharField(max_length=30)  # 字符串类型，最大长度为30
    file_path = models.CharField(max_length=30)  # 字符串类型，最大长度为30

    def __str__(self):  # 在admin站点中显示的名称
        return self.file_name

    class Meta:  # 元数据
        db_table = "file"  # 指定表名
        verbose_name = "文件"  # 指定在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
