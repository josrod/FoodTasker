from django.contrib import admin
from coreapp.models import Restaurant, Customer, Driver, Meal, Order, OrderDetails

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
