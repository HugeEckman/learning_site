from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Category, Lesson, User
from rest_framework.decorators import api_view
from .tasks import send_email_to_admin, send_email_to_user

import django_rq as rq
import redis

def index_view(request):
    return render(request, 'learning_app/index.html')

@api_view(['GET', 'POST'])
def contact_view(request):

    if request.method == 'POST':
        print(request.data['email'])
        print(request.data['subject'])
        print(request.data['message'])

        redis_conn = redis.StrictRedis()
        q = rq.get_queue(connection=redis_conn)

        q.enqueue(send_email_to_user)
        q.enqueue(send_email_to_admin)

    return render(request, 'learning_app/contacts.html')

# Courses


class CourseListView(ListView):
    model = Course
    template_name = 'learning_app/course_list.html' 


class CourseDetailView(DetailView):
    model = Course
    template_name = 'learning_app/course_detail.html' 

    # def get(self, request, *args, **kwargs):
    #     self.category_id = request.GET.get('category_id', None)
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        # quryset = queryset.filter(lesson__course__id=self.id)
        queryset = queryset.select_related('category')

        # queryset = queryset.prefetch_related('category')
        return queryset


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('learning_app:course_list')


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('learning_app:course_list')


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('learning_app:course_list')

# Categories


class CategoryListView(ListView):
    model = Category
    template_name = 'learning_app/category_list'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'learning_app/category_detail.html' 


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('learning_app:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('learning_app:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('learning_app:category_list')

# Lessons


class LessonListView(ListView):
    model = Lesson
    template_name = 'learning_app/lessons_list.html'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'learning_app/lessons_detail.html' 


class LessonCreateView(CreateView):
    model = Lesson
    fields = '__all__'
    success_url = reverse_lazy('learning_app:lessons_list')


class LessonUpdateView(UpdateView):
    model = Lesson
    fields = '__all__'
    success_url = reverse_lazy('learning_app:lessons_list')


class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('learning_app:lessons_list')

# Users


class UserListView(ListView):
    model = User
    template_name = 'learning_app/user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'learning_app/user_detail.html' 


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('learning_app:user_list')


class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('learning_app:user_list')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('learning_app:user_list')
