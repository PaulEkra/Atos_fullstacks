from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    users = User.objects.all()
    numbers_users = users.count()
    context = {
        'users': users,
        'total': numbers_users,
    }
    return render(request, "user/list.html", context)


def add_and_edit(request, pk=None):
    if pk:
        user = get_object_or_404(User, id=pk)
    else:
        user = None

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)

        if user_form.is_valid():
            user = user_form.save(commit=False)  
            password = request.POST.get('password', '')
            if password:  
                user.set_password(password)
            user.save()  
            return redirect('user:index')
        else:
            return render(request, 'user/forms.html', {"form": user_form})
    
    user_form = UserForm(instance=user)
    context = {
        "form": user_form
    }
    return render(request, "user/forms.html", context)

# def edit(request, id):
#   return render(request, "user/users_edit.html")
