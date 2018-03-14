from django.contrib import admin

from pay.models import Order

class Order_admin(admin.ModelAdmin):
    list_display=('subject','pk')

admin.site.register(Order,Order_admin)
