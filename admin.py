from django.contrib import admin

# Register your models here.
from.models import *
admin.site.register(product)
admin.site.register(Carts)
admin.site.register(Address)
admin.site.register(Orders)