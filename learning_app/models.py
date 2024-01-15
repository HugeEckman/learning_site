from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self) -> str:
        return self.name
    

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    goals = models.CharField(max_length=50)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.title



