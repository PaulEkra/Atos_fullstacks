from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "user/index.html")

def add(request):
    return render(request, "user/users_add.html")

def edit(request, id):
    return render(request, "user/users_edit.html")
