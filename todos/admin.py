from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at','completed')

admin.site.register(Todo, TodoAdmin)

## OR admin.site.register(Todo)