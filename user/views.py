from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import UserProfile
# from user.serializer import ProfileSerializer
from django.contrib.auth import authenticate,get_user_model  

# from .forms import UserProfileView

def login_view (request):
    _next=request.GET.get('next')
    form=UserProfileForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        if _next:
            return redirect()
        return redirect('/')
    context={
        'form':form,
    }

    return render(request, "login.html",context)




