from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from MovieFinder.accounts.forms import CustomUserCreationForm, CustomUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ['username', 'email', "is_staff", "is_superuser"]
    search_fields = ('username',)
    ordering = ('pk',)

    fieldsets = (
        ('Credentials', {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email",  "password1", "password2"),
            },
        ),
    )

