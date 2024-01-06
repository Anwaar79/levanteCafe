from django.db import models

# Create your models here.
class User(models.Model):
 staff_id = models.AutoField(primary_key=True)
 staff_name= models.CharField(max_length=100)
 staff_password= models.CharField(max_length=100)


 def __str__(self):
        return self.staff_name