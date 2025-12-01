from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

from shorts.views import ShortViewSet, ShortStatsViewSet

router = SimpleRouter()
router.register(r'', ShortViewSet)

nested_router = NestedSimpleRouter(router, r'', lookup='short')
nested_router.register(r'stats', ShortStatsViewSet, basename='short-stats')

urlpatterns = router.urls + nested_router.urls