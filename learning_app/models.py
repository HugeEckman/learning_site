from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    goals = models.CharField(max_length=50)
    # course = models.OneToOneField(Course, null=True, on_delete=models.SET_NULL)
    teacher = models.OneToOneField(Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title
    

class Course(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    finish_date = models.DateField()
    lessons = models.ForeignKey(Lesson, null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.name
    

class Catalog(models.Model):
    # course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    courses = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)



# class Schedule(models.Model):
#     pass


# class Role(models.Model):
#     pass

