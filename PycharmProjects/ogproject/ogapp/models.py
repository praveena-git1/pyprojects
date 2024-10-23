from django.db import models

# Create your models here.

class employee(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    joining_date = models.DateField()
    image=models.ImageField(upload_to='image/',default='profile.jpg')
    class Meta:
        db_table = "Employees"
