from django.contrib import admin

from .models import *

admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Catalog)
admin.site.register(Schedule)
admin.site.register(Lesson)