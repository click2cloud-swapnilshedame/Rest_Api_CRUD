from django.db import models


# Create your models here.
class Empmodels(models.Model):
    EmpID = models.IntegerField(primary_key=True)
    EmpName = models.CharField(max_length=70)
    Email = models.CharField(max_length=70)
    salary = models.IntegerField()

    class Meta:
        db_table = "Empmodels"

    def __str__(self):
        return self.EmpName