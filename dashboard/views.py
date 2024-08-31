from django.shortcuts import render, redirect
from user.forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from base.management.create_default_user import CreateDefaultUser

# Create your views here.
@login_required(redirect_field_name='next')
def index(request):
    return render(request, "dashboard/index.html")


def log_in(request):
    next_url=request.GET.get('next','')
    print(next_url)
    CreateDefaultUser().create_default_user("admin", "admin")  
     
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(next_url)
        messages.errors(request,"Veuillez entrer un username ou un mot de passe")

    form = UserForm()
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    context = {
        'form': form
    }
    return render(request, "login.html", context)

def log_out(request):
    logout(request)
    return redirect('')
