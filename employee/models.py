
from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    manager = models.ForeignKey(
        'manager.Manager',
        on_delete=models.CASCADE,
        related_name='employees'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
