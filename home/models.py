from datetime import timezone

from django.conf import settings
from django.contrib.auth.models import User, auth
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
import os
from random import randint
from django.utils.timezone import now
from datetime import date

def user_directory_path1(instance, filename):
    return 'user_{0}/video/{1}'.format(instance.instructor.id, filename)

def user_directory_path2(instance, filename):
    return 'user_{0}/pdf/{1}'.format(instance.instructor.id, filename)


def user_directory_path3(instance, filename):
    return 'user_{0}/banner/{1}'.format(instance.instructor.id, filename)


class Instructor( models.Model ):
    user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user' )
    Area_of_expert = models.CharField( max_length=30 )
    year_of_experience = models.IntegerField(
        default=1,
        validators=[MaxValueValidator( 20 ), MinValueValidator( 1 )]
    )
    department = models.CharField( max_length=50 )
    tutorial_experience = models.TextField( max_length=100 )
    help = models.BooleanField( default=False )

    def __str__(self):
        return self.user.username

today = str(date.today())
class Course( models.Model ):
    instructor = models.ForeignKey( Instructor, on_delete=models.CASCADE )
    date = models.CharField(max_length=10, blank=True, default=today)
    title = models.CharField( max_length=100 )
    doc_file = models.FileField(max_length=500, null=True, blank=True)
    description = models.TextField()
    amount = models.IntegerField()
    department = models.CharField( max_length=300 )
    pdf = models.FileField( upload_to=user_directory_path2)
    cover_pic = models.ImageField( upload_to=user_directory_path3 )
    like = models.ManyToManyField(User)
    duration = models.CharField(max_length=20)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class CourseFile(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    doc_file = models.FileField(max_length=500,   blank=False, null=False)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    docName = models.CharField(max_length=150, blank=True)
    thumbnailImage = models.FileField(max_length=500, null=True)
    duration = models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.course.title
    

class EnrolCourse( models.Model ):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    course = models.ForeignKey( Course, models.CASCADE )
    college = models.CharField( max_length=100, blank=True )
    date = models.CharField(max_length=10, blank=True, default=today)

    def __str__(self):
        return self.course.title


class College( models.Model ):
    college_name = models.CharField( max_length=100 )

    def __str__(self):
        return self.college_name


class Department( models.Model ):
    department_name = models.CharField( max_length=100 )
    college_faculty = models.ForeignKey( College, on_delete=models.CASCADE )

    def __str__(self):
        return self.department_name
