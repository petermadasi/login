from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model()   
# Create your views here.

@login_required
def UserDetailsView(request):
    return render(request,"userprofile.html",{})
# Create your views here.