#coding=utf-8
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name=u"名称", max_length=50)
    province = models.CharField(verbose_name=u'省公司', max_length=30)
    branch = models.CharField(verbose_name=u"分公司", max_length=30)
    
    def __unicode__(self):
        return self.name
    

class Member(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=30)
    department = models.ForeignKey('Department', null=True)
    user = models.OneToOneField('auth.User')
    
    
