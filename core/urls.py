from django.contrib import admin
from django.urls import path
from .views import PostListView, ReportCreateView
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ReportCreateView,
    FaqView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('report/', ReportCreateView.as_view(), name='report'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('filter/', views.filter, name='filter'),
    path('search-result/', views.search_result, name='search-result'),
    path('chat/', views.messages_page, name='chat'),
]