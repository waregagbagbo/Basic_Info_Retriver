# register our API routes

from django.urls import path
from .views import UserViewSet
urlpatterns =[
    path('', UserViewSet.as_view({'get': 'list','post':'create'})),
]