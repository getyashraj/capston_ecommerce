from django.contrib import admin
from .models import UserAccount, Address


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'phone',
        'first_name',
        'last_name',
        'address',
        'is_superuser',
        'is_staff',
        'is_active'
    )


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Address)
