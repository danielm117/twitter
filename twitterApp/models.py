from django.db import models
from django.utils.encoding import uri_to_iri

class Profile(models.Model):
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    password = models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.email)

