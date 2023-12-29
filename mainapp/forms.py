from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    model = User
    firlds=[ 'username','email','password1','password2']

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Cuorse
        fields = '__all__'

class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class CreateMentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'

class CreateMenteeForm(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = '__all__'

class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = '__all__'
    