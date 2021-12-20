from django.contrib import admin

# Register your models here.
from .models import IDE, Lang

admin.site.register(IDE)
admin.site.register(Lang)