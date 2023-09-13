from django.urls import path
from .views import PersonViewset

app_name = 'peopleAPI'

urlpatterns = [
    path('api/', PersonViewset.as_view({'get': 'list', 'post': 'create'}), name='person-list'),
    path('api/<str:pk>/', PersonViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='person-detail'),
]
