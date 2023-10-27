from django.contrib import admin
from .models import Product,Pedido,Detalle

# Register your models here.
admin.site.register(Product)
admin.site.register(Pedido)
admin.site.register(Detalle)