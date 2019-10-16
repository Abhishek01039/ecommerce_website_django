from django.db import models

# Create your models here.
class product(models.Model):
    pro_id=models.AutoField
    pro_name=models.CharField(max_length=30)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300)
    pro_date=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(default='',upload_to='shop/images')


    def __str__(self):
        return self.pro_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    email=models.CharField(max_length=50) 
    phone=models.CharField(max_length=10,default='')
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    add=models.CharField(max_length=150)
    add2=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=6,default="")

    def __str__(self):
        return self.name



class Update(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField()
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc