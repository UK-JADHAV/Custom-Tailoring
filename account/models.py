from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    name=models.CharField(max_length=100)
    measurements=models.TextField()
    neck=models.BinaryField()
    sleeves=models.BinaryField()
    waist=models.BinaryField()

    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(default='default.jpg',blank=True)
    customer=models.ForeignKey(User,default=None,on_delete=None)

    # add in author later


    def __str__(self):
        return self.name

    def snippet(self):
        return self.measurements[:50]+'......'
