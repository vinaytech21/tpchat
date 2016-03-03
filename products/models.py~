from __future__ import unicode_literals
import uuid
from django.db import models
from authtools.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User)
    title  = models.CharField(max_length=120)
    docfile = models.FileField(upload_to='Product/%Y/%m/%d',blank=True, null=True)
    #description = models.CharField(max_length=120)
    description = models.CharField(default=False, max_length=160)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    zip_Code = models.CharField(blank = True, max_length=6)
    address = models.CharField(default=False, max_length=60)
    date_created = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    date_Update = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(blank=True, null=True)
      
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("products")
        ordering = ("docfile",)

    def __unicode__(self):
        return self.docfile.path
