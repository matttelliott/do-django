from django.contrib import admin
from schema.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
