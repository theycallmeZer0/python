from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Article)

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarPass)
admin.site.register(TravelPoint)
admin.site.register(OwnerTravelPoint)
admin.site.register(DataOfPassingCar)