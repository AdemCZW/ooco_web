from django.contrib import admin
from .models import index


class index_01_Admin(admin.ModelAdmin):
    list_display = ()


admin.site.register(index)
