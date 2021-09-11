from datetime import datetime
from django.db import models




# class Testcase_Models(models.Model):
#     id = models.AutoField(primary_key=True)
#     nodeID = models.CharField(max_length=20)
#     remark = models.CharField(max_length=50,default=0)
#
#     class Meta:
#         db_table = "Testcase"
#
#
# class Task_models(models.Model):
#     id = models.AutoField(primary_key=True)
#     remark = models.CharField(max_length=50,default=0)
#     report = models.CharField(max_length=50,default='')
#     create_at = models.DateTimeField(default=datetime.now)
#
#     class Meta:
#         db_table = "Task"