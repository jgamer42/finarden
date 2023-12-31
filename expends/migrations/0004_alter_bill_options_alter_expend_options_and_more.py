# Generated by Django 4.2.7 on 2023-11-25 06:32

from django.db import migrations, models
import expends.models


class Migration(migrations.Migration):

    dependencies = [
        ('expends', '0003_bill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='expend',
            options={'verbose_name': 'Gasto', 'verbose_name_plural': 'Gastos'},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'Ingreso', 'verbose_name_plural': 'Ingresos'},
        ),
        migrations.RemoveField(
            model_name='bill',
            name='where',
        ),
        migrations.AlterField(
            model_name='bill',
            name='active',
            field=models.BooleanField(verbose_name='activo'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.FloatField(validators=[expends.models.min_max_values], verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='cutoff',
            field=models.IntegerField(validators=[expends.models.min_max_values, expends.models.max_date_value], verbose_name='fecha de corte'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='detail',
            field=models.TextField(verbose_name='detalle'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='duration',
            field=models.IntegerField(validators=[expends.models.min_max_values], verbose_name='cuotas'),
        ),
        migrations.AlterField(
            model_name='expend',
            name='amount',
            field=models.FloatField(validators=[expends.models.min_max_values], verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='expend',
            name='date',
            field=models.DateTimeField(verbose_name='fecha'),
        ),
        migrations.AlterField(
            model_name='expend',
            name='detail',
            field=models.TextField(verbose_name='detalle'),
        ),
        migrations.AlterField(
            model_name='expend',
            name='where',
            field=models.CharField(max_length=120, verbose_name='lugar'),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.FloatField(validators=[expends.models.min_max_values], verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(verbose_name='fecha'),
        ),
        migrations.AlterField(
            model_name='income',
            name='detail',
            field=models.TextField(verbose_name='detalle'),
        ),
        migrations.AlterField(
            model_name='income',
            name='source',
            field=models.CharField(max_length=120, verbose_name='fuente'),
        ),
    ]
