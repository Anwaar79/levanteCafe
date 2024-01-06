from django.db import models

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    Cal= models.IntegerField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='Levante/static/images/')

    BREAKFAST = "Breakfast"
    SOUP = "Soup"
    SALAD = "Salad"
    COLD_APPETIZERS = "Cold-Appetizers"
    HOT_APPETIZERS = "Hot-Appetizers"
    PIZZA = "Pizza"
    PASTA_RISOTTO = "Pasta-and-Risotto"
    SANDWICHES = "Sandwiches"
    MAIN_COURSES = "Main-Courses"
    GRILLED = "Grilled"
    FRESH_JUICE_SMOOTHIES = "Fresh-Juice-and-Smoothes"
    MOCKTAIL = "Mocktail"
    MILK_SHAKES_ICED_COFFEE = "Milk-shakes-and-Iced-Coffee"
    COFFEE_TEA = "Hot-Coffee-and-Tea"
    MINERAL_WATER_SOFT_DRINK = "Mineral-Water-and-Soft-Drink"
    SHISHA = "Shisha"

    ITEM_TYPE_CHOICES = [
    (BREAKFAST, "Breakfast"),
    (SOUP, "Soup"),
    (SALAD, "Salad"),
    (COLD_APPETIZERS, "Cold Appetizers"),
    (HOT_APPETIZERS, "Hot Appetizers"),
    (PIZZA, "Pizza"),
    (PASTA_RISOTTO, "Pasta and Risotto"),
    (SANDWICHES, "Sandwiches"),
    (MAIN_COURSES, "Main Courses"),
    (GRILLED, "Grilled"),
    (FRESH_JUICE_SMOOTHIES, "Fresh Juice and Smoothies"),  # Corrected spelling
    (MOCKTAIL, "Mocktail"),
    (MILK_SHAKES_ICED_COFFEE, "Milk shakes and Iced Coffee"),
    (COFFEE_TEA, "Hot Coffee and Tea"),
    (MINERAL_WATER_SOFT_DRINK, "Mineral Water and Soft Drink"),
    (SHISHA, "Shisha"),
]

    Food_Item_Type = models.CharField(
        max_length=28,
        choices=ITEM_TYPE_CHOICES,
        default=BREAKFAST,
    )

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['Food_Item_Type']