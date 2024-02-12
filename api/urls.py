from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .view_sets import CourseViewSet, RoleViewSet, CategoryViewSet, \
UserViewSet, LessonViewSet

router = DefaultRouter()

router.register('user', UserViewSet)
router.register('role', RoleViewSet)
router.register('course', CourseViewSet)
router.register('category', CategoryViewSet)
router.register('lesson', LessonViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]