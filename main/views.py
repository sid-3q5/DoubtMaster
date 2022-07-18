from platform import release
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib import auth
from .models import Profile, Student, Teacher, Doubt
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'main/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate account'
            message = render_to_string('main/acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'domain':"{0}".format("http://127.0.0.1:8000"),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage( mail_subject,message,to=[to_email])
            email.content_subtype = 'html'
            email.mixed_subtype = 'related'
            email.send()

            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            faculty = form.cleaned_data.get('faculty')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            profile = Profile.objects.create(user=user, phone=phone, gender=gender, faculty=faculty)

            if faculty == 'Tutor':
                Tutor = Teacher.objects.create(teacher=user)

            elif faculty == 'Student':
                student = Student.objects.create(student=user)
            return render(request,'main/confirm.html')
    else:
        form = SignupForm()   
    return render(request,'main/register.html',{'form':form})

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('login')
    else:  
        return HttpResponse('Activation link is invalid!')  

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        profile = Profile.objects.get(user=user)
        if user is not None:
            if profile.faculty == "Student":
                auth.login(request, user)
                pk = request.user.id
                return redirect(f"../stud_profile/{request.user.id}/")
            elif profile.faculty == "Tutor":
                auth.login(request, user)
                pk = request.user.id
                return redirect(f"../teacher_profile/{request.user.id}/")

        else:
            context = {'error': True}
            return render(request, 'main/login.html',context)  
    return render(request, 'main/login.html')  

def stud_profile(request ,pk):
    if  request.user.is_authenticated:
        student = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=student)
        std = Student.objects.get(student=student)
        r1 = Doubt.objects.filter(related=std.id)
        if request.method == 'POST':
            student = User.objects.get( pk=pk)
            profile = Profile.objects.get(user=student)
            r = Student.objects.get(student=student)
            r1 = Doubt.objects.filter(related=r.id)
            title = request.POST['title']
            description = request.POST['description']
            related = r
            doubt = Doubt.objects.create(title=title, description=description, related=related)
            context={"student":student, "profile":profile, 'r':r1}
            return render(request, 'main/stud_profile.html', context)
        context={"student":student, "profile":profile, 'r':r1}
        return render(request, 'main/stud_profile.html', context)
    else:
        return redirect("login")

def teacher_profile(request ,pk):
    if  request.user.is_authenticated:
        teacher = User.objects.get( pk=pk)
        profile = Profile.objects.get(user=teacher)
        l = Student.objects.values_list('student_id')
        c = Student.objects.count()
        stud = User.objects.all()
        pr = Profile.objects.all()
        # du = zip(pr,stud)
        context={"teacher":teacher, "profile":profile}
        return render(request, 'main/teacher.html', context)

    else:
        return redirect("login") 

# def doubt(request, pk):
#     if  request.user.is_authenticated:
#         student = User.objects.get( pk=pk)
#         profile = Profile.objects.get(user=student)
#         r = Doubt.objects.filter(related=profile.id)
#         context={"student":student, "profile":profile, "r":r}
#         return render(request, 'main/doubtadd.html', context)    
#     else:
#         return redirect("login")  
    