from django.urls import path

from api.views import check_imei

urlpatterns = [
    path('check-imei/', check_imei, name='check_imei'),
]
