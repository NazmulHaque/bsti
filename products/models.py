from django.db import models

class product(models.Model):
    type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    license_no = models.CharField(max_length=200)
    issue_date = models.DateField('issue_date')
    expire_date = models.DateField('expire_date')

    # def __unicode__(self):
    #     return self.name

# Create your models here.
