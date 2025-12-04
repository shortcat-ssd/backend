from django.contrib import admin

from shorts.models import Short, ShortClick

admin.site.register([Short, ShortClick])
