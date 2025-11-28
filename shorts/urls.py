from rest_framework.routers import SimpleRouter

from shorts.views import ShortViewSet, ShortStatsViewSet

router = SimpleRouter()
router.register(r'short', ShortViewSet)
router.register(r'stats', ShortStatsViewSet)

urlpatterns = router.urls
