from django.contrib import admin

from shorts.models import Short, ShortView

# Register your models here.

admin.site.register([Short, ShortView])
