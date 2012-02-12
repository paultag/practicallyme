from django.db import models

class Page(models.Model):
    owner      = models.ForeignKey('auth.User', primary_key=True)
    font       = models.CharField(max_length=50)
    title      = models.CharField(max_length=100)
    blurb      = models.TextField()
    background = models.CharField(max_length=256)
    website    = models.CharField(max_length=80)
    email      = models.EmailField()
