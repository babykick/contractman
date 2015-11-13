#coding=utf-8
from django.db import models
import uuid



# Create your models here.
class Project(models.Model):
    """ 项目
    """
    serial_number = models.CharField(max_length=50, verbose_name="项目编号", unique=True)
    name = models.CharField(max_length=50, verbose_name="项目名称")
    content = models.TextField(max_length=300, verbose_name="项目内容")
    

# Create your models here.
class Contract(models.Model):
    """ 合同
    """
    serial_number = models.CharField(max_length=50, verbose_name="合同编号", unique=True)
    name = models.CharField(max_length=50, verbose_name="合同名称")
    content = models.TextField(max_length=300, verbose_name="合同内容")
    fund = models.IntegerField(verbose_name="合同上限金额(万元)")
    important = models.BooleanField(default=False, verbose_name="重要性")
    
    
    
class WorkOrder(models.Model):
    """ 工单
    """
    serial_number = models.CharField(max_length=50, verbose_name="工单编号", unique=True)
    name = models.CharField(max_length=50, verbose_name="工单名")
    content = models.CharField(max_length=1000, verbose_name="工单内容")
    budget = models.PositiveIntegerField(verbose_name="工单预算")
    contract = models.ForeignKey(Contract)
    
    

    
    