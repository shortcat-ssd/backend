from django.contrib import admin

from shorts.models import Short, ShortView

admin.site.register([Short, ShortView])
