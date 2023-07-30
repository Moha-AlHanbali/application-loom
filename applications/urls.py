from django.urls import path
from .views import create_career_board, create_application

urlpatterns = [
    path('create_career_board/', create_career_board, name='create_career_board'),
    path('create/', create_application, name='create_application'),
]
