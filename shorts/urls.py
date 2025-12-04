from django.urls import path

from shorts.views import ShortsListView, ShortDetailsView, ShortClicksView

urlpatterns = [
    path("", ShortsListView.as_view()),
    path("<str:code>/", ShortDetailsView.as_view()),
    path("<str:code>/clicks/", ShortClicksView.as_view()),
]
