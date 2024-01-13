from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Category

def index_view(request):
    return render(request, 'learning_app/index.html')

class CourseListView(ListView):
    model = Course
    template_name = 'learning_app/course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'learning_app/course_detail.html' 


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



