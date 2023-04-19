from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.position} {self.department}'


class Employee(models.Model):
    full_name = models.CharField(max_length=30)
    year = models.DateField()
    salary = models.DecimalField(max_digits=19, decimal_places=10)
    job_title = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.full_name}-{self.job_title.name}'


