from pyexpat import model
from tabnanny import verbose
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountsInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"

class Customized(UserAdmin):
    inlines = (AccountsInline, )



admin.site.unregister(User)
admin.site.register(User, Customized)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Doubt)