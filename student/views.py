from django.shortcuts import render, get_object_or_404, redirect

from .forms import StudentForm
from .models import Student
from datetime import datetime


# Create your views here.
def index(request):
    students = Student.objects.all()
    today = datetime.now().year

    context = {
        'students': students,
        'today': today,
    }
    return render(request, "student/list.html", context)


def add_and_edit(request, pk=None):
    if pk:
        student = get_object_or_404(Student, id=pk)
    else:
        student = None
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:index')

    form = StudentForm(instance=student)
    context = {
        'form': form
    }
    return render(request, "student/forms.html", context)


# def edit(request, id):
#     return render(request, "student/student_edit.html")


def delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return redirect('student:index')
