from django.contrib import admin

from reviews.models import Category, Genre, Title, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category')
    list_filter = ('year', 'genre', 'category')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name',
        'last_name', 'role', 'is_superuser',
    )
    list_editable = ('role',)
    search_fields = ('username', 'email')
    list_filter = ('role',)
