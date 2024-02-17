from rest_framework.serializers import ModelSerializer, Serializer
from learning_app.models import *

class CourseModelSerializer(ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'

# class RoleModelSerializer(ModelSerializer):

#     class Meta:
#         model = Role
#         fields = '__all__'
        
class TeacherModelSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class LessonModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class TecherModelSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'