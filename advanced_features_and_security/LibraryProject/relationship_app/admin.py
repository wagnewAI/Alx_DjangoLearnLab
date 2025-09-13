from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Author, Book, Library, Librarian


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "role", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
