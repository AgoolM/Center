from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models  import *
from django.core.paginator import Paginator
# Create your views here.
#@login_required(login_url='login')
def logistic_content_page(request):
    videoss=VideoContent.objects.all()
    page=Paginator(videoss,1)
    page_list=request.GET.get('page')
    page=page.get_page(page_list)

    videos = VideoContent.objects.filter(category="Logistic")
    context = {
        "videos" : videos,
        'page' :page
    }
    return render(request, "mainapp/videos_logistic.html", context)

def base_page(request):
    return render (request, 'mainapp/base.html')

#@login_required(login_url='login')
def dashbord(request):
    mentees=Mentee.objects.all()
    context={
        'mentees':mentees
    }
    return render(request,'mainapp/dashbord.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return render('dashbord')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashbord")
            else:
                messages.info(request,"Something was wrong")  

        context = {}

        return render(request,'mainapp/login.html', context)


def register_user(request):
    if request.user.is_superuser:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid:
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('login')
        context = {
            "form":form
        }
        return render(request, 'mainapp/register.html',context)
    else:
        return redirect('dashbord')
    




def logout_user(request):
    logout(request)
    return redirect('login')


def course_cerate(request):
    if request.user.is_superuser:
        form = CreateCourseForm()
        if request.method == "POST":
            form = CreateCourseForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('course_t')
            else:
                form = CreateCourseForm()

        context = {
            "form" : form
        }
        
        return render(request, 'mainapp/course_cerate.html', context)
    else:
        return redirect('dashbord')

#@login_required(login_url='login')

def mentor_create(request):
    if request.user.is_superuser:
        form = CreateMentorForm()
        if request.method == "POST":
            form = CreateMentorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mentor_t')
            else:
                form = CreateMenteeForm()

        context = {
            "form" : form
        }
        
        return render(request, 'mainapp/mentor_cerate.html', context)
    else:
        return redirect('dashbord')
    

def mentor_table(request):
    if request.user.is_superuser:
        mentors = Mentor.objects.all().order_by('full_name')
        context = {
            'mentors' : mentors
        }
        return render(request, 'mainapp/mentor_teble.html', context)
    else:
        return redirect('dashbord')
    

def update_mentor(request, pk):
    if request.user.is_superuser:
        mentors = Mentor.objects.get(id=pk)
        form  = CreateMentorForm(instance=mentors)
        if request.method == "POST":
            form = CreateMentorForm(request.POST, instance=mentors)
            if form.is_valid:
                form.save()
                return redirect('mentor_t')

        context = {
            "form" : form
        }

        return render(request, "mainapp/mentor_cerate.html", context)
    else:
        return redirect('dashbord')
    

def delete_mentor(request, pk):
    if request.user.is_superuser:
        mentors = Mentor.objects.get(id=pk)
        if request.method == "POST":
            mentors.delete()
            return redirect('mentor_t') 
        context = {
            'mentors':  mentors
        }
        return render(request, 'mainapp/mentor_delet.html', context)
    else:
        return redirect('dashbord')


def mentee_create(request):
    if request.user.is_superuser:
        form = CreateMenteeForm()
        if request.method == "POST":
            form = CreateMenteeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mentee_t')
            else:
                form = CreateMenteeForm()

        context = {
            "form" : form
        }
        
        return render(request, 'mainapp/mentee_create.html', context)
    else:
        return redirect('dashbord')
    

def mantee_table(request):
    if request.user.is_superuser:
        mentees = Mentee.objects.all().order_by('full_name')
        context = {
            'mentees' : mentees
        }
        return render(request, 'mainapp/mente_table.html', context)
    else:
        return redirect('dashbord')
    

def update_mentee(request, pk):
    if request.user.is_superuser:
        mentees = Mentee.objects.get(id=pk)
        form  = CreateMenteeForm(instance=mentees)
        if request.method == "POST":
            form = CreateMenteeForm(request.POST, instance=mentees)
            if form.is_valid:
                form.save()
                return redirect('mentee_t')

        context = {
            "form" : form
        }

        return render(request, "mainapp/mentee_create.html", context)
    else:
        return redirect('dashbord')

def delete_mentee(request, pk):
    if request.user.is_superuser:
        mentees = Mentee.objects.get(id=pk)
        if request.method == "POST":
            mentees.delete()
            return redirect('mentee_t') 
        context = {
            'mentees': mentees
        }
        return render(request, 'mainapp/mentee_delete.html', context)
    else:
        return redirect('dashbord')
    





def course_table(request):
    if request.user.is_superuser:
        courses = Cuorse.objects.all().order_by('title')
        context = {
            'courses' : courses
        }
        return render(request, 'mainapp/course_table.html', context)
    else:
        return redirect('dashbord')



def update_course(request, pk):
    if request.user.is_superuser:
        course =Cuorse.objects.get(id=pk)
        form  = CreateCourseForm(instance=course)
        if request.method == "POST":
            form = CreateCourseForm(request.POST, instance=course)
            if form.is_valid:
                form.save()
                return redirect('course_t')

        context = {
            "form" : form
        }

        return render(request, "mainapp/course_cerate.html", context)
    else:
        return redirect('dashbord')



#CRUD-CourseView - Delete
#@login_required(login_url='login')
def delete_course(request, pk):
    if request.user.is_superuser:
        course = Cuorse.objects.get(id=pk)
        if request.method == "POST":
            course.delete()
            return redirect('course_t') 
        context = {
            'course': course
        }
        return render(request, 'mainapp/course_delete.html', context)
    else:
        return redirect('dashbord')


def group_cerate(request):
    if request.user.is_superuser:
        form = CreateGroupForm()
        if request.method == "POST":
            form = CreateGroupForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('group_t')
            else:
                form = CreateGroupForm()

        context = {
            "form" : form
        }
        
        return render(request, 'mainapp/group_creat.html', context)
    else:
        return redirect('dashbord')



def update_group(request, pk):
    if request.user.is_superuser:
        group =Group.objects.get(id=pk)
        form = CreateGroupForm(instance=group)
        if request.method == "POST":
            form = CreateCourseForm(request.POST, instance=group)
            if form.is_valid:
                form.save()
                return redirect('group_t')

        context = {
            "form" : form
        }

        return render(request, "mainapp/group_create.html", context)
    else:
        return redirect('dashbord')



def delete_group(request, pk):
    if request.user.is_superuser:
        group =Group.objects.get(id=pk)
        if request.method == "POST":
            group.delete()
            return redirect('group_t') 
        context = {
            'group': group
        }
        return render(request, 'mainapp/group_delet.html', context)
    else:
        return redirect('dashbord')


def group_table(request):
    if request.user.is_superuser:
        groups = Group.objects.all().order_by('title')
        context = {
            'groups' : groups
        }
        return render(request, 'mainapp/group_tabel.html', context)
    else:
        return redirect('dashbord')



def video_cerate(request):
    form = CreateVideoForm()
    if request.method == "POST":
        form = CreateVideoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('logistic')
        else:
            form = CreateCourseForm()

    context = {
        "form" : form
    }
    
    return render(request, 'mainapp/video_create.html', context)

def delete_video(request, pk):
    videos = VideoContent.objects.get(id=pk)
    if request.method == "POST":
        videos.delete()
        return redirect('logistic') 
    context = {
        'videos': videos
    }
    return render(request, 'mainapp/video_delet.html', context)


def update_video(request, pk):
    videos = VideoContent.objects.get(id=pk)
    form  = CreateVideoForm(instance=videos)
    if request.method == "POST":
        form = CreateVideoForm(request.POST, instance=videos)
        if form.is_valid:
            form.save()
            return redirect('logistic')

    context = {
        "form" : form
    }

    return render(request, "mainapp/video_create.html", context)



