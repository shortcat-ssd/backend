from django.contrib import admin

from shorts.models import Short, ShortStats

# Register your models here.

admin.site.register([Short, ShortStats])
