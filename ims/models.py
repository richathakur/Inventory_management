from django.db import models

# Create your models here.
class items(models.Model):
    item_name = models.CharField(max_length=40, null=True, verbose_name="item_name * ")    
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name="quantity")    
    item_type = models.CharField(max_length=40, null=True, verbose_name="item_type * ") 
    mode = models.CharField(max_length=40, null=True, verbose_name="mode_of_transport * ")
    transport_number = models.IntegerField(null=True,  verbose_name="transport Number * ")   
    present_address = models.CharField(max_length=100, null=True, blank=True,verbose_name="Present_Address")    
    Delivery_location = models.CharField(max_length=100, null=True, blank=True,verbose_name="Delivery_Address")   
    def __str__(self):
        return f"{self.item_name}"
        return f"{self.quantity}"
        return f"{self.item_type}"
        return f"{self.mode_of_transport}"
        return f"{self.present_address}"
        return f"{self.transport_number}"
        return f"{self.Delivery_location}"
