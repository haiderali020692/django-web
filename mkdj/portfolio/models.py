from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # Add other fields as needed

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # If you have a User model for authentication
    items = models.ManyToManyField('CartItem')
    

class CartItem(models.Model):
    product = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)