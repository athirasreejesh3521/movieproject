from django.db import models



# Create your models here.
class Service(models.Model):
    type=models.CharField(max_length=500)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')


    def __str__(self):
        return self.type