from django.urls import path, include
from send_email.views import ClienteViewSet, EnvioViewSet
from rest_framework import routers


app_name = 'send_email'
router = routers.DefaultRouter()
router.register('clientes',ClienteViewSet, basename='Clientes')
router.register('envios',EnvioViewSet, basename= 'Envios')

urlpatterns = [
    path('', include(router.urls))
]
