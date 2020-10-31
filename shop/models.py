from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=500)
    category = models.CharField(max_length=100, default="")
    sub_category = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/pro_image",default="")
    product_desc = models.TextField()
    published_date = models.DateField()
    

    def __str__(self):
        return self.product_name
    


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone = models.IntegerField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    

    def __str__(self):
        return self.name + " | " + self.subject
    














