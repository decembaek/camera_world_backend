from django.contrib import admin
from .models import User

# Register your models here.
# admin.site.register(User)
# admin.py


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "nickname", "is_staff")
    search_fields = ("email", "name", "nickname")
    ordering = ("email",)


# admin.py
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.utils.translation import gettext, gettext_lazy as _
# from .models import User


# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         (_("Personal info"), {"fields": ("name", "nickname", "avatar")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "password1", "password2"),
#             },
#         ),
#     )
#     list_display = ("email", "name", "nickname", "is_staff")
#     search_fields = ("email", "name", "nickname")
#     ordering = ("email",)


# admin.site.register(User, UserAdmin)
