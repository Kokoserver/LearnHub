from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from home.models import Course, Instructor, CourseFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import re


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        url  = request.POST['next']
        check_if_user_exists = User.objects.filter(username=username).exists()
        if  username == '' and password == '':
            messages.error(request, 'Please, fill in your details!')
            return HttpResponseRedirect('/user/')
        elif password == '':
            messages.error(request, 'Password is required, please enter your Password!')
            return HttpResponseRedirect('/user/')
        elif  username == '':
              messages.error(request, 'Username is required, please enter your Username!')
              return HttpResponseRedirect('/user/') 
        elif check_if_user_exists:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(url)
            else:
                 messages.error(request, 'Wrong password provided')
                 return HttpResponseRedirect('/user/')
            # this user is not valid, he provided wrong password, show some error message 
        else:  
            messages.error(request, 'Account does not exist')
            return HttpResponseRedirect('/user/')
    else:
        if request.user.is_authenticated:
            return redirect(url)
        elif not request.user.is_authenticated:
            return render(request, 'login.html')
        

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    rx_name = re.compile("^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$") 
    rx_username = re.compile('^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*$')
    rx_email = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain
    
    # checking if the request from browser is post or get
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmpassword']
        username = request.POST['username']
        url = request.POST['next']
        # checking if the fields are not empty
        if first_name == '' and last_name== '' and email == '' and pass1 == '' and pass2 == '':
            messages.error(request, 'Please fill all your details to continue!')
            return redirect('/user/register')
        if first_name == '':
                messages.error(request, 'First name is required')
                return HttpResponseRedirect('/user/register', {'first_name': first_name})
        elif last_name == '':
                messages.error(request, 'Last name is required')
                return HttpResponseRedirect('/user/register',{'last_name': last_name})
            
        elif email == '':
                messages.error(request, 'Email is required')
                return HttpResponseRedirect('/user/register', {'email': email})
            
        elif username == '':
                messages.error(request, 'Username name is required')
                return HttpResponseRedirect('/user/register', {'username': username}) 
        elif pass1 == '':
                messages.error(request, 'Password name is required')
                return HttpResponseRedirect('/user/register', {'pass1': pass1})
        elif pass2 == '':
                messages.error(request, 'Confirm your password')
                return HttpResponseRedirect('/user/register', {'pass2': pass2})
        elif pass1 != pass2:
                messages.error(request, 'Sorry password does not match') 
                return HttpResponseRedirect('/user/register')
        else:
            # checking for validity of the field entered
            if  rx_name.match(request.POST['first_name']):
                first_name = request.POST['first_name']
            else:
                messages.error(request, 'First name can only contain charater between a-z')
                return HttpResponseRedirect('/user/register')
                
            if  rx_name.match(request.POST['last_name']):
                last_name = request.POST['last_name']
            else:
                messages.error(request, 'Last name can only contain charater between a-z')
                return HttpResponseRedirect('/user/register')
                
            if  rx_email.match(request.POST['email']):
                email = request.POST['first_name']
            else: 
                messages.error(request, 'Enter a valid email')
                return HttpResponseRedirect('/user/register')
            
            if  rx_username.match(request.POST['username']):
                username= request.POST['username']
            else:
                messages.error(request, 'Invalid username') 
                return HttpResponseRedirect('/user/register')  
            if pass1 == pass2:
                password = pass1
            else:
                messages.error(request, 'password does not match') 
                return HttpResponseRedirect('register')
            
            if not re.search('[a-zA-Z]+', password) or not re.search('[0-9]+', password):
              messages.error(request,'Your password must include at least \
                                       one letter and at least one number.')
              return HttpResponseRedirect('register')
               
            
            
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name)
                user.save()
                
                auth.authenticate(username=username, password=password)
                if user is not None:
                  auth.login(request, user)
                  return redirect(url)
            else:
                messages.error(request, 'User with this Username already exist') 
                return HttpResponseRedirect('/user/register')
                 
    return render(request, 'register.html')


def account(request):
  if request.user.is_authenticated:
    account_details = User.objects.get(pk=request.user.id)
    username = account_details.username
    password = account_details.password
    user_account = auth.authenticate(username=username, password=password)
    course = Course.objects.all().filter(instructor_id=request.user.id)
    video = CourseFile.objects.all().filter(instructor_id=request.user.id)
    pdf = Course.objects.values('pdf').distinct().count()
    paginator = Paginator(course, 5)
    page = request.GET.get('page')
    try:
        courseList = paginator.page(page)
    except PageNotAnInteger as pnt:
        courseList = paginator.page(1)
    except EmptyPage: 
        courseList = paginator.page(paginator.num_pages)
        
        
    try: 
        instructor = request.user.id == Instructor.objects.get(id=request.user.id)
        isInstructor = True
       
    except Instructor.DoesNotExist:
        isInstructor = False     
    context =  {'user': account_details, 
                'course':course,
                'video': video, 
                'pdf':pdf,
                'page': page, 
                'courseList':courseList,
                'isInstructor': isInstructor
                }
    return render(request, 'account.html', context)
  else: 
      return redirect('/')
  
def setting(request):
    return render(request, 'settings.html')

