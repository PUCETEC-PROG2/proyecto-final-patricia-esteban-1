# Generated by Django 5.1.6 on 2025-02-15 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugueteria_pechan', '0003_rename_cantidad_compra_total_alter_articulo_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='category',
            field=models.CharField(choices=[('6 a 12 meses', '6 a 12 meses'), ('objetos decorativos', 'objetos decorativos'), ('muebles', 'muebles'), ('11 a 14 años', '11 a 14 años'), ('ropa', 'ropa'), ('5 a 8 años', '5 a 8 años'), ('herramientas', 'herramientas'), ('3 a 5 años', '3 a 5 años'), ('0 a 6 meses', '0 a 6 meses'), ('1 a 2 años', '1 a 2 años')], max_length=45),
        ),
    ]
