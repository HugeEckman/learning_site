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
    
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('lesson/list/<int:pk>', views.LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', views.LessonDeleteView.as_view(), name='lesson_delete'),
]