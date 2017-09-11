from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # 如果不手动指定，则默认生成id列，自增，主键
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    user_group = models.ForeignKey("UserGroup",to_field='uid') # (uid,catption,ctime,uptime)


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)
