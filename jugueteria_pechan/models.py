from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
    


class Articulo(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    ARTICULOS_CATEGORY = {
        ('0 a 6 meses', '0 a 6 meses'),
        ('6 a 12 meses', '6 a 12 meses'),
        ('1 a 2 años', '1 a 2 años'),
        ('3 a 5 años', '3 a 5 años'),
        ('5 a 8 años', '5 a 8 años'),
        ('11 a 14 años', '11 a 14 años'),
        ('ropa', 'ropa'),
        ('muebles', 'muebles'),
        ('herramientas', 'herramientas'),
        ('objetos decorativos', 'objetos decorativos')
    }
    category = models.CharField(max_length=45, choices=ARTICULOS_CATEGORY, null=False)
    picture = models.ImageField(upload_to="articulos_images")
    
    def __str__(self):
        return self.nombre
    
    
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    articulo = models.ManyToManyField(Articulo)
    fecha_compra = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Compra {self.id} - Cliente: {self.cliente.nombre} - Total: {self.total}"

@receiver(m2m_changed, sender=Compra.articulo.through)
def update_total(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.total = sum(articulo.precio for articulo in instance.articulo.all())
        instance.save()