from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User


# Create your models here.
class Notebook(models.Model):
    user = models.ForeignKey(User, default=1)
    notebook_title = models.CharField(max_length=500)
    notebook_description = models.CharField(max_length=250,null=True)


    class Meta:
        unique_together = ('user', 'notebook_title',)

    def get_absolute_url(self):
        return reverse('wowCS:index')

    def __str__(self):
        return self.notebook_title


class Note(models.Model):
    notebook = models.ForeignKey(Notebook,on_delete= models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, default=1)
    note_title = models.CharField(max_length=200)
    note_content = models.TextField()
    # public/private status
    ispublic = models.BooleanField(default=True)
    # the count of marked as favorite.
    favorite_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('wowCS:catalogue',kwargs={'notebook_title':self.notebook})

    def __str__(self):
        return self.note_title


class Favorite(models.Model):
    user = models.ForeignKey(User, default=1)
    favorite_id = models.IntegerField()

    class Meta:
        unique_together = ('user', 'favorite_id',)




