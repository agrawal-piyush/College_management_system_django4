from django.db import models
class Student(models.Model):
    S_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    Branch = models.CharField(max_length=30)
    Year = models.IntegerField()


