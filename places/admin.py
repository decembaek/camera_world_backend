from django.contrib import admin

from .models import Place

# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     list_display =

admin.site.register(Place)
