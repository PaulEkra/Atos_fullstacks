from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "teacher/index.html")

def add(request):
    return render(request, "teacher/teachers_add.html")

def edit(request, id):
    return render(request, "teacher/teachers_edit.html")

def delete(request):
    pass
