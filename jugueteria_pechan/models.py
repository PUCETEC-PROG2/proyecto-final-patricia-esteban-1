from django.db import models


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
    articulo = models.ForeignKey(Articulo, on_delete=models.SET_NULL, null=True)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente}"