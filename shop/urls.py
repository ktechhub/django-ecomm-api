


from shop.views import apiOverview
from django.urls import path

urlpatterns = [
    path('', apiOverview),
]
