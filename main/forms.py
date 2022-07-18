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


    first_name = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Doubt','class':''}))

    last_name = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Master','class':''}))

    username = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={  'placeholder':'Username','class':''}))
    
    email = forms.EmailField(max_length=100, label='',help_text='Required', widget=forms.TextInput(attrs={'placeholder':'admin@gmail.com','class':''}))

    password1 = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Password','type':'password','class':''}))

    password2 = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Confirm password','type':'password','class':''}))

    phone = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Phone','class':''}))

    CHOICES = [('Male','Male'),('Female','Female')]

    gender = forms.ChoiceField(label='Gender',widget=forms.RadioSelect, choices=CHOICES)
    country = forms.CharField(max_length=30, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Country','class':''}))
    state = forms.CharField(max_length=30, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'State','class':''}))
    address = forms.CharField(max_length=100, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Address','class':''}))
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

