from django.db import models
from manager.models import Manager

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE
    )