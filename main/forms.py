from cProfile import label
from dataclasses import field
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doubt


class SignupForm(UserCreationForm):
    # email = forms.EmailField(max_length=200, label = '',help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Email','class':'input'}))
    # first_name = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'First name','class':'input'}))
    # last_name = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Last name','class':'input'}))
    # phone = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Phone','class':'input'}))
    # password1 = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Password','type':'password','class':'input', 'id':'myInput'}))
    # check69 = forms.BooleanField(label='Show Password',widget= forms.CheckboxInput(attrs={'onclick':'myFunction()'}))
    # password2 = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Confirm password','type':'password','class':'input'}))
    # username = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={  'placeholder':'Username','class':'input'}))
    # CHOICES = [('Male','Male'),('Female','Female')]
    # CHOICES1 = [('Tutor','Tutor'), ('Student', 'Student')]
    # faculty=forms.CharField(label='Register as', widget=forms.RadioSelect(choices=CHOICES1,attrs={'class':'input2'}))
    # gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES,attrs={'class':'input2'}))
    # gender = forms.ChoiceField(choices=(("Male","Male"),("Female", "Female")), widget=forms.RadioSelect(attrs={"label":"Gender"}))
    # gender = forms.ChoiceField(label='gender',widget=forms.RadioSelect, choices=CHOICES)


    first_name = forms.CharField(max_length=200, label = 'First Name', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Doubt','id':'name'}))

    last_name = forms.CharField(max_length=200, label = 'Last Name', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Master','id':'name'}))

    username = forms.CharField(max_length=200, label = 'Username', help_text='Required',widget= forms.TextInput(attrs={  'placeholder':'Username','class':''}))
    
    email = forms.EmailField(max_length=100, label='Email',help_text='Required', widget=forms.TextInput(attrs={'placeholder':'doubtmastera@gmail.com','id':'email'}))

    password1 = forms.CharField(max_length=200, label = 'Password', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Password','type':'password','id':'password'}))

    password2 = forms.CharField(max_length=200, label = 'Confirm Password', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Confirm password','type':'password','id':'password'}))

    phone = forms.CharField(max_length=200, label = 'Phone', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Phone','id':'name'}))

    CHOICES = [('Male','Male'),('Female','Female')]

    gender = forms.ChoiceField(label='Gender',widget=forms.RadioSelect, choices=CHOICES)
    country = forms.CharField(max_length=30, label = 'Country', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'India','id':'name'}))
    state = forms.CharField(max_length=30, label = 'State', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Maharashtra','id':'name'}))
    address = forms.CharField(max_length=100, label = 'Address', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Gittikhadan,Nagpur','id':'name'}))
    CHOICES1 = [('Tutor','Tutor'), ('Student', 'Student')]
    faculty=forms.CharField(label='Register as', widget=forms.RadioSelect(choices=CHOICES1,attrs={'class':''}))


    class Meta:
        model=User
        fields = ('first_name','last_name','username','email','password1', 'password2','phone','gender','faculty','country','state','address')


class DoubtListForm(forms.Form):
    title = forms.CharField(max_length=30,label='Title')
    description = forms.CharField(max_length=200, label="Description")

    class Meta:
        model=Doubt
        fields = ('tilte','description')

