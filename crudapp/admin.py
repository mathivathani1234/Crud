from django.contrib import admin

# Register your models here.
from .models import * # Add closing parenthesis here

admin.site.register(CrudappModel)
