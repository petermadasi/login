from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate,get_user_model
from .models import UserProfile


User=get_user_model()

class UserProfileForm(forms.Form):
    Username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    phone=forms.CharField()
    address =forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('phone', 'address')

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = UserChangeForm.Meta.fields

