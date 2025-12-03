"""
URL configuration for shortcat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi, views
from rest_framework import permissions, schemas
from shorts.util import redirect_short

schema_view = views.get_schema_view(
    openapi.Info(
        title="Shortcat API",
        default_version="v1",
        description="Shortcat API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

ADMIN_ROUTE = os.environ.get("DJANGO_ADMIN_ROUTE", "admin").rstrip("/")

urlpatterns = [
    path(f"{ADMIN_ROUTE}/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path(
        "swagger.<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("schema/", schemas.get_schema_view(title="Shortcat API"), name="schema"),
    path("api/v1/shorts/", include("shorts.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("<str:code>/", redirect_short),
]
