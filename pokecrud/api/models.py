from django.db import models

# Create your models here.
class Api(models.Model):
    name=models.CharField(max_length=40)
    image = models.ImageField(
        blank=True, upload_to='static/images', default='static/images/no-image.jpg')

    def __str__(self):
        return self.name