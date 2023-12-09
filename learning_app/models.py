from django.db import models


class Role(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Course(models.Model):
    name = models.CharField(max_length=50)
    category_id = models.OneToOneField(Category, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)


class Catalog(models.Model):
    course_id = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)


class Schedule(models.Model):
    pass


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    goals = models.CharField(max_length=50)
    teacher_id = models.OneToOneField(Teacher, null=True, on_delete=models.SET_NULL)


