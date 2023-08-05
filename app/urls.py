from .views import video
from django.urls import path 

urlpatterns = [
    path('', video),
    
]