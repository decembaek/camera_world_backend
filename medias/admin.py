from django.contrib import admin
from .models import Photo

# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     list_display =

admin.site.register(Photo)
