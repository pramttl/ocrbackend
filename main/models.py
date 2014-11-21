from django.db import models

# Create your models here.

class Image(models.Model):
    photo = models.FileField(upload_to="photos")
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % unicode(self.photo)
