from rest_framework.serializers import ModelSerializer, Serializer
from learning_app.models import *

class CourseModelSerializer(ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'
