from django.contrib import admin
from .models import MyModel

# Register your models here.

 
@admin.register(MyModel)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
MyModel._meta.get_fields()]