from django.db import models

# Create your models here.
class book(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',default='profile.jpg')
    class Meta:
        db_table = "bookadd"
