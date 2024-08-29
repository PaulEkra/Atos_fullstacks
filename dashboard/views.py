from django.shortcuts import render
from user.forms import UserForm


# Create your views here.
def index(request):
    return render(request, "dashboard/index.html")


def login(request):
    form = UserForm()

    context = {
        'form': form
    }
    return render(request, "login.html", context)
