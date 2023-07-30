from django.urls import path
from .views import create_career_board, career_board_list, create_application

urlpatterns = [
    path('create_career_board/', create_career_board, name='create_career_board'),
    path('career_board_list/', career_board_list, name='career_board_list'),

    path('create/', create_application, name='create_application'),
]
