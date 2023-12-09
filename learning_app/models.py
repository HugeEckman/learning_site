from django.db import models
# from django import  


class Role(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Course(models.Model):
    name = models.CharField()
    category = models.OneToOneField(Category, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

class Catalog(models.Model):
    pass

class Schedule(models.Model):
    pass

class Lesson(models.Model):
    pass