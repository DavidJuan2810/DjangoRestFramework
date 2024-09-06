from rest_framework import routers
from django.urls import include, path
from .views import TareaViewSet

router = routers.DefaultRouter()
router.register(r'tareas',TareaViewSet)

urlpatterns = [
    path('',include(router.urls))
]