from rest_framework.urls import path

from shorts.views import ShortList, ShortDetails, ShortViewsList

urlpatterns = [
    path('', ShortList.as_view(), name='short-list'),
    path('<str:code>/', ShortDetails.as_view(), name='short-detail'),
    path('<str:code>/views/', ShortViewsList.as_view(), name='short-stats-detail'),
]