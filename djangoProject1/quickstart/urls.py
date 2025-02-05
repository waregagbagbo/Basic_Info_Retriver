# register our API routes

from django.urls import path
from .views import UserViewSet
urlpatterns =[
    #manually map HTTP methods to the actions in the Viewset class
    path('', UserViewSet.as_view({'get': 'list'})),
]