
from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)
app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(),name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(),name='article-detail'),

    path('create/', ArticleCreateView.as_view(),name='article-create'), #rendering with initial data
    path('<int:pk>/update/', ArticleUpdateView.as_view(),name='article-update'), #rendering with initial data
    path('<int:pk>/delete/', ArticleDeleteView.as_view(),name='article-delete'),
    

]
