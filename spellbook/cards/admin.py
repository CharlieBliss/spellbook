from django.contrib import admin
from .models import Card
# Register your models here.
@admin.register(Card)
class AuthorAdmin(admin.ModelAdmin):
    pass