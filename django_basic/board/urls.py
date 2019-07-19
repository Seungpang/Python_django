from django.urls import path
from . import views

urlpatterns = [
    path('api/board', views.api_board_write),
    path('api/detail/<int:pk>', views.api_board_detail),
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write),
]
