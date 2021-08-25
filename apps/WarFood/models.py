from django.db import models
class producto(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    codigo = models.CharField(max_length=9, null=False, blank=False)
    name = 10
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

class Cliente(models.Model):
    pk_id = models.AutoField(primary_key=True, null=False, blank=False)
    Nombre = models.TextField(max_length=80, default="n/a", null=False, blank=False)
    Apellido = models.TextField(max_length=80, default="n/a", null=False, blank=False)
    Tarjeta = models.IntegerField(null=False, blank=False)
    Identificacion = models.IntegerField(null=False, blank=False)
    Ncontacto = models.IntegerField(max_length= 8,null=False, blank=False)
    Ubicacion = models.TextField(max_length=150, default="n/a", null=False, blank=False)

class Menu(models.Model):
    pk_id = models.AutoField(primary_key=True, null=False, blank=False)
    Nfactura = models.IntegerField(max_length= 12,null=False, blank=False)
    total_a_pagar = models.IntegerField(null=False, blank=False)
    fk_Productos = models.TextField(max_length=80, default="n/a", null=False, blank=False)

class Mesa(models.Model):
    pk_Nmesa = models.AutoField(primary_key=True, null=False, blank=False)
    reservacion = models.BooleanField(null=False)
    Cantidad_Sillas = models.IntegerField(max_length=8, null=False, blank=False)

class Trabajador(models.Model):
    pk_id = models.AutoField(primary_key=True, null=False, blank=False)
    Nombre = models.TextField(max_length=80, default="n/a", null=False, blank=False)
    Apellido = models.TextField(max_length=80, default="n/a", null=False, blank=False)
    DPI = models.IntegerField(null=False, blank=False)
    Puesto = models.TextField(max_length=80, default="n/a", null=False, blank=False)

class Factura(models.Model):
    pk_Nfactura = models.AutoField(primary_key=True, null=False, blank=False)
    Cantidad = models.CharField(max_length=2, null=False, blank=False)
    fk_clientes = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fk_Menu = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.CASCADE)
    fk_Mesa = models.ForeignKey(Mesa, null=False, blank=False, on_delete=models.CASCADE)
    fk_Trabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)