from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ArticleListView,
    TextCreateView,
    TextListView,
)



urlpatterns = [
    path('', PostListView.as_view(), name="klas-home"),
    path('',TextListView.as_view(), name="klas-home-text"),
    path('article/', ArticleListView.as_view(), name="klas-article"),
    path('text/', TextCreateView.as_view(), name="text-home"),
    path('user/<str:username>/',UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('admisi/', views.admisi, name='klas-admisi'),
    path('schedule/', views.schedule, name="klas-schedule"),
    #path('booking/', views.booking, name="booking")
    path('booking/', views.booking, name="booking"),


]
