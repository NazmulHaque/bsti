from django.db import models

class organization(models.Model):
    name = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)

    # def __unicode__(self):
    #     return self.name