from django.db import models
from table.models import Table
from menu.models import Item
from django.utils import timezone

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    table_choice = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    date_created = models.DateTimeField(default=timezone.now)

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items.all())
        return total_price

    def __int__(self):
        return self.order_id