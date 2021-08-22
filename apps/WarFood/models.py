from django.db import models
class producto(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    codigo = models.CharField(max_length=9, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False,blank=False)
    price = models.DecimalField(null=False, max_digits=2, decimal_places=2)

class stock(models.Model):
    ps_stock = models.AutoField(primary_key=True, null=False, blank=False)
    amount = models.IntegerField(null=False,blank=False)
    fk_producto = models.OneToOneField(producto, null=False, blank=False, on_delete=models.CASCADE)

class sell(models.Model):
    pk_sell = models.AutoField(primary_key=True, null=False, blank=False)
    name_client = models.CharField(max_length=80, default="n/a", null=False, blank=False)
    date_buy = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    fk_producto = models.ForeignKey(producto, null=False, blank=False, on_delete=models.CASCADE)
# Create your models here.
