from rest_framework.viewsets import ModelViewSet
from learning_app.models import *
from .serialyzers import CourseModelSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer