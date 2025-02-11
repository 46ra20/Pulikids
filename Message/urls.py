from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MessageView

router = DefaultRouter()
router.register(r'',MessageView,basename="message")

urlpatterns = [
    path("",include(router.urls))
]
