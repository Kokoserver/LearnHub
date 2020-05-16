import os
import subprocess
import math
from LearnHub import settings
import random 
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import CourseForm
import string
from .models import Instructor, User, Course, CourseFile
from moviepy.editor import VideoFileClip

media_url = settings.MEDIA_URL
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
# ffmpeg = os.path.join(PROJECT_ROOT, 'ffmpeg/bin/ffmpeg.exe')
# ffprobe = os.path.join(PROJECT_ROOT, 'ffmpeg/bin/ffprobe.exe')
# media = os.path.join(PROJECT_ROOT, 'media/temp')
thumbnailPath = os.path.join(PROJECT_ROOT, 'media/thumbnail')
finalPath = os.path.join(PROJECT_ROOT, f'media/upload')




# Create your views here.
def index(request):
    course = Course.objects.all().order_by( 'date' )[::-1][:5]
    like = Course.objects.all().order_by( 'like' )[:10]
    csc = Course.objects.filter( department__iexact='computer science' ).count()
    math = Course.objects.filter( department__iexact='mathematics' ).count()
    bioch = Course.objects.filter( department__iexact='biochemistry' ).count()
    account = Course.objects.filter( department__iexact='accounting' ).count()
    is_active = True
    context = {'active': is_active,
               'course': course,
               'like': like,
               'csc': csc,
               'account': account,
               'math': math,
               'bioch': bioch

               }
    return render( request, 'index.html', context )


def partner(request):
    return render( request, 'index.html' )


def lecturer(request):
    if request.method == 'POST':
        Area_of_expert = request.POST['areaOfExpert']
        year_of_experience = request.POST['yearOfExperience']
        department = request.POST['department']
        tutorial_experience = request.POST['tutorialExperience']
        helpline = True
        if Area_of_expert == '' and year_of_experience == '' and department == '' and tutorial_experience == '':
            messages.error( request, 'Please file in the form to continue' )
            return redirect( 'lecturer' )
            if year_of_experience == '':
                messages.error( request, 'Please enter how long you have been a teacher/lecture if non enter 1' )
                return redirect( 'lecturer' )
            if department == '':
                messages.error( request, 'Enter the department you will like to teach' )
                return redirect( 'lecturer' )
            if tutorial_experience == '':
                messages.error( request,
                                'Have you done any online course training before if yes enter, if no Enter novice' )
                return redirect( 'lecturer' )
        else:
            instructor = Instructor( Area_of_expert=Area_of_expert, year_of_experience=year_of_experience,
                                     department=department, tutorial_experience=tutorial_experience,
                                     help=helpline )
        instructor.user = User.objects.get( pk=request.user.pk )
        instructor.save()
        return redirect( 'lectures' )
    else:
        if not request.user.id:
            return HttpResponseRedirect( '/user/register' )
        else:
            try:
                var = Instructor.objects.get( user_id=User.objects.get( pk=request.user.pk ) )
                return HttpResponseRedirect( 'lectures' )

            except Instructor.DoesNotExist:
                return render( request, 'lecturer.html' )


def lectures(request):
    form = CourseForm()
    context = {
        'form': form
    }
    return render( request, 'lectures.html', context )


def randomString(stringLength):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
     
def getDuration(filePath): 
    video = VideoFileClip(filePath)   
    duration =float(video.duration) 
    hour = math.floor(duration/3600)
    minute = math.floor((duration-(hour*3600))/60)
    seconds = math.floor(duration%60)
    if hour<1:
        hour=""
    else:
        hour = f"{hour}:"
    if minute < 10:
        minute = f"0{minute}:"
    else:
        minute = f"{minute}:"
    if seconds < 10 and seconds > 0:
       seconds = f"0{seconds}"
    else: 
        seconds 
    Duration = f"{hour}{minute}{seconds}"
    return Duration


def getThumbnail(filePath):
    thumbnail = VideoFileClip(filePath)
    thumbnailId = randomString(8)
    thumbnailImage = f"{thumbnailPath}/{thumbnailId}thumbnail.png"
    thumbnail.save_frame(thumbnailImage, t=1.00)
    return  thumbnailImage
    
            
# def converter(course, instructor, userid):
#             inputdir = media
            
#             outputdir = finalPath
#             for file in os.listdir(outputdir):
#                 # sourceVideo = inputdir + '/' + file
#                 if file.endswith('.mp4'):
#                     continue
#                 else:
#                     destinationVideo = outputdir + '/' + file[:-4] + ".avi"
#                     finalFile = outputdir + '/' + file[:-4] + ".mp4"
#                     totalDuration = getDuration(destinationVideo)
#                     thumbnail = getThumbnail(destinationVideo)
#                     clip = VideoFileClip(destinationVideo)
#                     clip.write_videofile(finalFile, codec='libx264')
#                     os.unlink(destinationVideo)
                    
#                 # command = [ffmpeg, '-i', sourceVideo, '-vb',  '20M' ,'-vcodec', 'libx264', destinationVideo]
#                 # try:
#                 #     subprocess.call(command)
#                 # except FileExistsError as identifier:
#                 #     continue
                
#                 # os.remove(sourceVideo)
#                 docname = file[8:][:-4]
#                 docname.replace(file[9:], "")
#                 docname.replace(file[:-4], "")
#                 totalDuration = getDuration(destinationVideo)
#                 thumbnail = getThumbnail(destinationVideo)
#                 doc = CourseFile(course=course, doc_file=destinationVideo, instructor=instructor, docName=docname, duration=totalDuration, thumbnailImage=thumbnail)
#                 doc.save()
                
# path = "/Users/owoni/projects/learnHub/media/upload/1x6ymi4o_20051210-w50s_56K.flv"
# extention = str(path[:-4])
# newpath = path[:-4] + ".avi"
# # print(newpath)

@csrf_protect
def upload(request):
    if request.method == 'POST':
        form = CourseForm( request.POST, request.FILES )
        instructor = Instructor.objects.get( user_id=User.objects.get( pk=request.user.pk ) )
        files = request.FILES.getlist('doc_file')
        id = request.user.id
        if form.is_valid():
            course_details = form.save( commit=False )
            course_details.doc_file = ""
            course_details.instructor = instructor
            for count, x in enumerate(request.FILES.getlist("doc_file")):
                randomId = randomString(8)
                def process(f):
                       path = finalPath+f'/{randomId}_{f.name}'
                       name = f.name[:-4]
                       with open(path, 'wb+') as destination:
                        for chunk in f.chunks():
                          destination.write(chunk) 
                        thumbnail = getThumbnail(path) 
                        duration = getDuration(path)
                        doc = CourseFile(course=course_details, doc_file=path, instructor=instructor, docName=name, duration=duration, thumbnailImage=thumbnail)
                        doc.save() 
                process(x)
            course_details.save()
        return redirect('/')
                    
    else:
        return redirect( '/' )
                

                                 
        
    

    

def like(request):
    if request.method == 'POST':
        courseId = request.POST.get( 'id' )
        course = get_object_or_404( Course, id=courseId )
        user = request.user
        if user.is_authenticated:
            if user in course.like.all():
                course.like.remove( user )
                like = course.like.count()
            else:
                course.like.add( user )
                like = course.like.count()

        else:
            pass
    return JsonResponse( {'count': like} )


def view(request, id):
    if request.user.is_authenticated:
        course = Course.objects.get( id=id )
        doc_fileList = CourseFile.objects.all().order_by( 'id' )
        video = CourseFile.objects.all().filter( course_id=course ).order_by( 'id' )
        context = {
            'course': course,
            'video': video
        }
        return render( request, 'video-page.html', context )
    else:
        return render( request, 'login.html' )


def details(request, id):
    details = Course.objects.get(id=id)
    related_course  = Course.objects.all().filter(department=details.department).order_by('id')
    return None


def bestselling():
    return None


def bestrating(request):
    return render( request, "subscriptions.html" )
    return None


def myCourse():
    return None
