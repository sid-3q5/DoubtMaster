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
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import get_user_model
from django.contrib import auth
from .models import Profile, Student, Teacher, Doubt, List
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
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            address = form.cleaned_data.get('address')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            profile = Profile.objects.create(user=user, phone=phone, gender=gender, faculty=faculty, country=country, state=state, address=address)

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
            context={"student":student, "profile":profile, 'r':r1, 'r1':r}
            return render(request, 'main/stud_profile.html', context)
        context={"student":student, "profile":profile, 'r':r1, 'pk':pk}
        return render(request, 'main/stud_profile.html', context)
    else:
        return redirect("login")

def doubtlist(request, pk):
    if  request.user.is_authenticated:
        student = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=student)
        std = Student.objects.get(student=student)
        r1 = Doubt.objects.filter(related=std.id)
        context={"student":student, "profile":profile, 'r':r1}
        return render(request, 'main/doubtlist.html', context)
    else:
        return redirect("login")

def teacher_profile(request ,pk):
    if  request.user.is_authenticated:
        teacher = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=teacher)
        tech = Teacher.objects.get(teacher=teacher)
        r = Doubt.objects.filter(answer='Unanswered').values()
        context={"teacher":teacher, "profile":profile, "r":r}
        return render(request, 'main/teacher.html', context)
    else:
        return redirect("login") 

def doubt(request,pk):
    if  request.user.is_authenticated:
        r = Doubt.objects.get( pk=pk )
        l = List.objects.filter(doubt=pk)
        context={"r":r, "l":l}
        return render(request, 'main/doubt.html', context)
    else:
        return redirect("login")      

def test1(request,pk):
    if  request.user.is_authenticated:
        r = Doubt.objects.get( pk=pk )
        pf = request.user.id
        teach = User.objects.get(pk=pf)
        teacher = Teacher.objects.get(teacher=teach)
        k = List.objects.filter(teacher=teacher, doubt=r)
        if k.exists():
            # ALREADY EXIST
            already_exist = True
            
            context={"r":r,"already_exist":already_exist}
            return render(request, 'main/tech_doubt.html', context)
        else:
            if request.method == 'POST':
                amount = request.POST['amount']
                description = request.POST['description']
                duration = request.POST['duration']
                pf = request.user.id
                teach = User.objects.get(pk=pf)
                teacher = Teacher.objects.get(teacher=teach)
                list1 = List.objects.create(amount=amount, description=description, duration=duration, doubt=r, teacher=teacher)
                context={"r":r}
                return render(request, 'main/tech_doubt.html', context)
        context={"r":r}
        if request.method == 'POST':
            amount = request.POST['amount']
            description = request.POST['description']
            duration = request.POST['duration']
            pf = request.user.id
            teach = User.objects.get(pk=pf)
            teacher = Teacher.objects.get(teacher=teach)
            list1 = List.objects.create(amount=amount, description=description, duration=duration, doubt=r, teacher=teacher)
            context={"r":r}
            return render(request, 'main/tech_doubt.html', context)
        
        return render(request, 'main/tech_doubt.html', context)
    else:
        return redirect("login")    

def test2(request,pk):
    if  request.user.is_authenticated:
        r = List.objects.get( pk=pk )
        context={"r":r}
        return render(request, 'main/offered.html', context)
    
    else:
        return redirect("login")  

def pay(request,pk):
    if  request.user.is_authenticated:
        r = List.objects.get( pk=pk )
        
        if request.method == 'POST':
            confirm = request.POST['confirm']
            if confirm == 'Yes' or confirm == 'yes':
                r = List.objects.get( pk=pk )
                ids = r.doubt.id
                idt = r.teacher.id
                rate = r.teacher.rating
                g = Doubt(id=ids, answer='Answered')
                g1 = Teacher(id=idt, rating=rate+10)
                g.save(update_fields=['answer'])
                g1.save(update_fields=['rating'])
                context={"r":r}
                return render(request, 'main/offered.html', context)
            else:
                err = 'Type Correctly'
                context={"r":r, "err":err}
                return render(request, 'main/payment.html', context)
        context={"r":r}
        return render(request, 'main/payment.html', context)
    
    else:
        return redirect("login")  

def logout(request):
    auth.logout(request)
    return redirect("/") 
