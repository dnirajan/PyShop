from django.contrib import admin
#username Admin
#pw Admin123
# Register your models here.
from .models import Products,Offers


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')


admin.site.register(Offers,OfferAdmin)

admin.site.register(Products,ProductAdmin)
