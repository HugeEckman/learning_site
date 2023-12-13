from django.urls import path

from . import views

app_name = 'learning_app'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('course/list/', views.CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),

]