from django.db import models

class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=12)

    def __unicode__(self):
        return self.name