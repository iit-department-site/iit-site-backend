from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/<int:pk>', views.SubscribeFollowerView.as_view()),
    path('unsubscribe/<int:pk>', views.UnsubscribeFollowerView.as_view()),
    path('list', views.ListFollowerView.as_view())
]
