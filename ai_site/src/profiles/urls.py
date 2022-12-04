from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.UserNetView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('profile/update/<int:pk>', views.UserNetView.as_view({'put': 'update'})),
    path('profile/create', views.UserNetView.as_view({'post': 'create'})),
    path('profile/<int:pk>/avatar', views.UserAvatarView.as_view(
        {'post': 'upload_avatar', 'put': 'upload_avatar', 'get': 'get_avatar'}
    )),
    path('technology/<int:pk>', views.TechnologyViewSet.as_view({'get': 'retrieve'})),
    path('technology/update/<int:pk>', views.TechnologyViewSet.as_view({'put': 'update'})),
    path('technology/create', views.TechnologyViewSet.as_view({'post': 'create'})),
    path('technology/<int:pk>/image', views.TechnologyImageViewSet.as_view(
        {'post': 'upload_tech_image', 'put': 'upload_tech_image', 'get': 'get_tech_image'}
    )),
    path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'}), name="public-user"),
]
