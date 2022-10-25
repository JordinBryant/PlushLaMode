from django.contrib import admin
from .models import Accessory, Dress
# from .models import Review
# Register your models here.

admin.site.register(Dress)
admin.site.register(Accessory)
# admin.site.register(Review)