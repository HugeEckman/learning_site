from rest_framework.viewsets import ModelViewSet
from learning_app.models import *
from .serialyzers import CourseModelSerializer, RoleModelSerializer, \
CategoryModelSerializer, UserModelSerializer, LessonModelSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CourseViewSet(ModelViewSet):

    autentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer