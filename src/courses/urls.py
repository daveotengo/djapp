
from django.urls import path

from .views import (
    CourseView,
    #MyListView
    CourseListView,
    # CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)
app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(),name='course-list'),
    path('<int:pk>/', CourseView.as_view(),name='course-detail'),

    path('create/', CourseCreateView.as_view(),name='course-create'), #rendering with initial data
    path('<int:pk>/update/', CourseUpdateView.as_view(),name='course-update'), #rendering with initial data
    path('<int:pk>/delete/', CourseDeleteView.as_view(),name='course-delete'),
    

]
