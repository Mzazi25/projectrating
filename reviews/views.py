from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Project,Rating
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()


# Create your views here.
@login_required(login_url='accounts/login/')
def dashboard(request):
    project = Project.objects.all()
    
    #adding context
    project = {'project':project}
    return render(request,'dashboard.html', project)