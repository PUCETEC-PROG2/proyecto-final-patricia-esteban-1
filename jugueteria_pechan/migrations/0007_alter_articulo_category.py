# Generated by Django 5.1.6 on 2025-02-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugueteria_pechan', '0006_alter_articulo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='category',
            field=models.CharField(choices=[('ropa', 'ropa'), ('6 a 12 meses', '6 a 12 meses'), ('herramientas', 'herramientas'), ('5 a 8 años', '5 a 8 años'), ('3 a 5 años', '3 a 5 años'), ('0 a 6 meses', '0 a 6 meses'), ('11 a 14 años', '11 a 14 años'), ('muebles', 'muebles'), ('objetos decorativos', 'objetos decorativos'), ('1 a 2 años', '1 a 2 años')], max_length=45),
        ),
    ]
