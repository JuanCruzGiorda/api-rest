from django.db import models

# Create your models here.
Tipos = (
    ('hamburguesa','Hamburguesa'),
    ('acompañamiento','Acompañamiento')
    
)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(upload_to='products', default='imagen_default.png', verbose_name='Imagen')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    description = models.TextField(verbose_name='Descripcion')
    tipe = models.CharField(choices=Tipos, max_length=200, verbose_name='Tipo')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Pedido(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Detalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    
    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['pedido']
    
    def __str__(self):
        return self.pedido