from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ServicesViewSet

router = DefaultRouter()
router.register(r'', ServicesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]