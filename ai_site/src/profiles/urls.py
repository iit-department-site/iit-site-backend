from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserNetView.as_view({'get': 'retrieve', 'put': 'update'}), name="private-user"),
    path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'}), name="public-user"),
]
