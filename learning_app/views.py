from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from models import Course


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

