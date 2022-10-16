from django.urls import path
from . import views

urlpatterns = [
    path('comment/create', views.CommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>', views.CommentsView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('comment/update/<int:pk>', views.CommentsView.as_view({'put': 'update'})),
    path('post/create', views.PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', views.PostView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('post/update/<int:pk>', views.PostView.as_view({'put': 'update'})),
    path('post/all', views.PostListView.as_view()),
]
