from django.contrib import admin

from reviews.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name',
        'last_name', 'role', 'is_superuser',
    )
    list_editable = ('role',)
    search_fields = ('username', 'email')
    list_filter = ('role',)
