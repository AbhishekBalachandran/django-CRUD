from django.db import models
from django.urls import reverse 

# Create your models here.


class Medicine(models.Model):
    """Model representing a medicine"""
    product_name = models.CharField(max_length=200,help_text='name of the medicine',null=True)

   
    name_of_manufacturer = models.CharField(max_length=200,null=True,help_text='name of the manufacturer')
    
    price = models.IntegerField('M.R.P', help_text='Enter the MRP value of the medicine',null=True)

    description = models.TextField(max_length=2000, help_text='Enter a short description on the product',null=True)
    
    date_of_manufacture = models.DateField(null=True, blank=True,help_text='Date of the product manufacture')
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('medicine-detail', args=[str(self.id)])