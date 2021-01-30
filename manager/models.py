from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=3000,default="Company")

    def __str__(self):
        return u'{0}'.format(self.company_name)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    post_date = models.DateField(default=timezone.now())
    amount = models.IntegerField()
    description = models.TextField(max_length=3000,default="job")
    requirements = models.TextField(max_length=3000,default="not specified")
    




   