from django.urls import  path
from . import views


urlpatterns = [
    path('', views.FeedView.as_view({'get': 'list'}),)
]