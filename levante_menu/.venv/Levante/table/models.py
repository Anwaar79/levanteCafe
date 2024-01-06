from django.db import models
class Table(models.Model):
     table_id = models.AutoField(primary_key=True)
     table_name= models.CharField(max_length=20, null=True)

     def __str__(self):
        return str(self.table_id)