# Generated by Django 5.1.6 on 2025-02-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugueteria_pechan', '0002_alter_articulo_category_alter_compra_articulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='cantidad',
            new_name='total',
        ),
        migrations.AlterField(
            model_name='articulo',
            name='category',
            field=models.CharField(choices=[('3 a 5 años', '3 a 5 años'), ('muebles', 'muebles'), ('0 a 6 meses', '0 a 6 meses'), ('11 a 14 años', '11 a 14 años'), ('objetos decorativos', 'objetos decorativos'), ('1 a 2 años', '1 a 2 años'), ('herramientas', 'herramientas'), ('5 a 8 años', '5 a 8 años'), ('ropa', 'ropa'), ('6 a 12 meses', '6 a 12 meses')], max_length=45),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='articulo',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='compra',
            name='articulo',
            field=models.ManyToManyField(to='jugueteria_pechan.articulo'),
        ),
    ]
