#coding=utf-8
from __future__ import division
from django.db import models
from company.models import Department
import uuid



# Create your models here.
class Project(models.Model):
    """ 项目
    """
    serial_number = models.CharField(max_length=50, primary_key=True, verbose_name="项目编号", unique=True)
    name = models.CharField(max_length=50, verbose_name="项目名称")
    intro = models.TextField(max_length=300, verbose_name="项目介绍", default="")
    department = models.ForeignKey(Department, verbose_name="所属部门", null=True, related_name='projects')
    pm = models.ForeignKey('company.Member', verbose_name="项目负责人", default=1)
    budget = models.DecimalField(verbose_name=u"批复开支费用(万元)",  max_digits=8, decimal_places=2, default=0)
    material_cost = models.DecimalField(verbose_name=u"材料费用(万元)", max_digits=8, decimal_places=2, default=0)
    construction_cost = models.DecimalField(verbose_name=u"施工费用(万元)", max_digits=8, decimal_places=2, default=0)
    supervision_cost = models.DecimalField(verbose_name=u"监理费用(万元)", max_digits=8, decimal_places=2, default=0)
    coordination_cost = models.DecimalField(verbose_name=u"协调费用(万元)", max_digits=8, decimal_places=2, default=0) 
    other_cost = models.DecimalField(verbose_name=u"其他费用(万元)", max_digits=8, decimal_places=2, default=0)
    
    
    def total_cost(self):
        return self.material_cost + self.construction_cost + self.supervision_cost + self.coordination_cost + self.other_cost
    
    def cost_percent(self):
        return "{0:2.0f}%".format(self.total_cost() / self.budget * 100)
    
    def left_fund(self):
        return self.budget - self.total_cost()
    
    
    def __unicode__(self):
        return self.name
    
    
# Create your models here.
class Contract(models.Model):
    """ 合同
    """
    TYPES = ((u'constuction', u'施工'),
              (u'material', u'材料'))
    serial_number = models.CharField(max_length=50, primary_key=True, verbose_name="合同编号", unique=True)
    name = models.CharField(max_length=50, verbose_name="合同名称")
    content = models.TextField(max_length=300, verbose_name="合同内容")
    fund_limit = models.DecimalField(verbose_name="合同上限金额(万元)", max_digits=8, decimal_places=2, default=0)
    used_fund = models.DecimalField(verbose_name="已完成投资(万元)", max_digits=8, decimal_places=2, default=0)
    partA = models.CharField(verbose_name="甲方", max_length=50)
    partB = models.CharField(verbose_name="乙方", max_length=50)
    timeline = models.CharField(max_length=30, verbose_name="时限(年-月-日)")
    project = models.ForeignKey('Project', related_name='contracts')
    contract_type = models.CharField(max_length=30, choices=TYPES,default='construction')
     
     
    def cost_percent(self):
        return "{0:2.0f}%".format(self.used_fund  / self.fund_limit * 100)
    
    def fundWarning(self):
        return self.used_fund  / self.fund_limit * 100 > 80
    
    def left_fund(self):
        return  self.fund_limit - self.used_fund
    
    
class WorkOrder(models.Model):
    """ 工单
    """
    serial_number = models.CharField(max_length=50, verbose_name="工单编号", unique=True)
    name = models.CharField(max_length=50, verbose_name="工单名")
    content = models.CharField(max_length=1000, verbose_name="工单内容")
    budget = models.PositiveIntegerField(verbose_name="工单预算")
    contract = models.ForeignKey(Contract)
    
    

    
    