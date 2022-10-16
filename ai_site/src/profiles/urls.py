from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.UserNetView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('profile/update/<int:pk>', views.UserNetView.as_view({'put': 'update'})),
    path('profile/create', views.UserNetView.as_view({'post': 'create'})),
    path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'}), name="public-user"),
]
