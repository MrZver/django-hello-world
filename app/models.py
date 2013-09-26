# Create your models here.
from django.db import models
from datetime import datetime


class User1(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()
    bio = models.TextField(max_length=300)
    email = models.EmailField(max_length=30, unique=True)
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField(max_length=300)

    class Meta:
        db_table = 'user_table'

    def __unicode__(self):
        return '{0} {1} ({2})'.format(self.first_name, self.last_name, self.email)


