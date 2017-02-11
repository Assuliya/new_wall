from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

def moreThanTwo(value):
      if len(value) < 3:
          raise ValidationError(
              'Must be longer than 2'
          )


class User(models.Model):
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255, validators = [moreThanTwo])
    last_name = models.CharField(max_length=255, validators = [moreThanTwo])
    password = models.CharField(max_length=255, validators = [moreThanTwo])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return u"%s" % (self.first_name)

class Post(models.Model):
    post = models.TextField()
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % (self.title)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % (self.comment)
