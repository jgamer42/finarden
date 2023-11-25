from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def min_max_values(value):
    if value < 1:
        raise ValueError
def max_date_value(value):
    if value > 31:
        raise ValueError
class Expend(models.Model):
    detail = models.TextField(verbose_name="detalle")
    amount = models.FloatField(verbose_name="valor",validators=[min_max_values])
    date = models.DateTimeField(verbose_name="fecha")
    where = models.CharField(max_length=120,verbose_name="lugar")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
    
class Income(models.Model):
    detail = models.TextField(verbose_name="detalle")
    amount = models.FloatField(verbose_name="valor",validators=[min_max_values])
    date = models.DateTimeField(verbose_name="fecha")
    source = models.CharField(max_length=120,verbose_name="fuente")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"
    
class Bill(models.Model):
    detail = models.TextField(verbose_name="detalle")
    duration = models.IntegerField(verbose_name="cuotas",validators=[min_max_values])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cutoff = models.IntegerField(verbose_name="fecha de corte",validators=[min_max_values,max_date_value])
    amount = models.FloatField(verbose_name="valor",validators=[min_max_values])
    active = models.BooleanField(verbose_name="activo")
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
    
