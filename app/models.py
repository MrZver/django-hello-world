# Create your models here.
from django.db import models
from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30, unique=True, help_text='Enter valid email address')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        pass

    def __unicode__(self):
        return '{0} {1} ({2})'.format(self.first_name, self.last_name, self.username)


class Message(models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.message_text[0:30]

