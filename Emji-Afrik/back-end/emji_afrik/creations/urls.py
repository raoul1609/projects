from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CreationViewset

router = DefaultRouter()
router.register(r'', CreationViewset)

urlpatterns = [
    path('', include(router.urls)),
]