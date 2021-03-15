from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=30, null=True)
    telfirst_name=models.CharField(max_length=30, null=True)
    last_name=models.CharField(max_length=30, null=True)
    telegram_id=models.TextField(max_length=30, null=False)
    telegram_hash=models.CharField(max_length=30, null=True)
    phone=models.CharField(max_length=30,null=True)
    def __str__(self):
        return ''
class Group(models.Model):
    group_title = models.CharField(max_length=50, null=False)
    group_id = models.CharField(max_length=30, null=True)
    member_id=models.CharField(max_length=30, null=True)
    last_name=models.CharField(max_length=30, null=True)
    telegram_id=models.TextField(max_length=30, null=False)
    telegram_hash=models.CharField(max_length=30, null=True)
    phone=models.CharField(max_length=30,null=True)
    def __str__(self):
        return ''