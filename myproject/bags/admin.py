from django.contrib import admin
from.models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Suppliers)
admin.site.register(Payment)

