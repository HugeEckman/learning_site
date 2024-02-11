from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .view_sets import CourseViewSet

router = DefaultRouter()
router.register('course', CourseViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]