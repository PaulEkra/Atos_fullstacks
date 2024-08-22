from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "student/index.html")

def add(request):
    return render(request, "student/student_add.html")

def edit(request,id):
    return render(request, "student/student_edit.html")

def delete(request):
    pass
