import graphene
from graphene_django import DjangoObjectType

from learning_app.models import User, Teacher, Course, Category, Lesson

class UserType(DjangoObjectType):
    class Meta:
        model = User
        field = '__all__'


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        field = '__all__'


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        field = '__all__'


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        field = '__all__'


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson
        field = '__all__'


class Query(graphene.ObjectType):

    user_list = graphene.List(UserType)

    def resolve_user_list(self, info):
        return User.objects.all()
    
    teacher_list = graphene.List(TeacherType)

    def resolve_teacher_list(self, info):
        return Teacher.objects.all()

    course_list = graphene.List(CourseType)

    def resolve_course_list(self, info):
        return Course.objects.all()
    
    category_list = graphene.List(CategoryType)

    def resolve_category_list(self, info):
        return Category.objects.all()
    
    lesson_list = graphene.List(LessonType)

    def resolve_lesson_list(self, info):
        return Lesson.objects.all()


schema = graphene.Schema(query=Query)
