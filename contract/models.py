#coding=utf-8
from django.db import models

# Create your models here.
class Contract(models.Model):
    title = models.CharField(max_length=50, verbose_name="合同标题")
    content = models.TextField(max_length=300, verbose_name="合同内容")
    