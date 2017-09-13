from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=44)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
    user_id = models.ForeignKey(User)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    user_id = models.ForeignKey(User)
    comment_id = models.ForeignKey(Message)
    comment = TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
