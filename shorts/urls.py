from django.urls import path

from shorts.views import ShortsListView, ShortDetailsView, ShortViewsView

urlpatterns = [
    path("", ShortsListView.as_view()),
    path("<str:code>/", ShortDetailsView.as_view()),
    path("<str:code>/views/", ShortViewsView.as_view()),
]
