from django.db import models


class Linkedinleads(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name ='id') 
    name = models.TextField(max_length=100, verbose_name ='name')  
    link = models.TextField(max_length=500, verbose_name ='Link')  
    dateinvite = models.DateField(blank=True,  null=True, verbose_name ='DateInvitation')
#   date_add = models.DateField(blank=True,  verbose_name ='Date Add')

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        ordering = ['id']

class Assets(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name ='id') 
    name = models.TextField(max_length=100, verbose_name ='name')
    user = models.TextField(max_length=100, verbose_name ='user')
    email = models.TextField(max_length=100, verbose_name ='email')
    password = models.TextField(max_length=12, verbose_name ='password')  