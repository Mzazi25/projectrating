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

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_category = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='accounts/login/')
def profile(request):
    
    if request.method == 'POST':
        data = request.POST
                       
        project = Project.objects.create(
            name = data['p-name'],
            owner = request.user,
            link = data ['p-link'],
            description = data['description'],
                               
        )
        return redirect('profile')
    current = request.user.pk
    profile = Profile.objects.filter(username=current).all()
    project = Project.objects.filter(description=current).all()
    prj={'profile':profile,'project':project}
    return render(request,'profile.html',prj)