from django.contrib import admin
from .models import Instructor, Course, EnrolCourse, College,Department, CourseFile
# Register your models here.
admin.site.register(Instructor)
admin.site.register(EnrolCourse)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseFile)

