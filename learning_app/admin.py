from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Catalog)
admin.site.register(Lesson)
# admin.site.register(Role)
# admin.site.register(Schedule)