from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view_sets import CourseViewSet, TeacherViewSet, CategoryViewSet, \
UserViewSet, LessonViewSet

router = DefaultRouter()

router.register('user', UserViewSet)
# router.register('role', RoleViewSet)
router.register('teacer', TeacherViewSet)

router.register('course', CourseViewSet)
router.register('category', CategoryViewSet)
router.register('lesson', LessonViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]