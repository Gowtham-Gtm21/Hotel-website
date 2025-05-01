from django.db import models

# Create your models here.

class Items(models.Model):    
    Image = models.ImageField(upload_to='items/')
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField()

    def __str__(self):
        return self.Item_name

class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
    
