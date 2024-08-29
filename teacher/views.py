from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .forms import TeacherForm
from .models import Teacher


# Create your views here.
def index(request):
    teachers = Teacher.objects.all()
    today = datetime.now().year
    numbers_teacher = teachers.count()
    context = {
        'teachers': teachers,
        'total': numbers_teacher,
        'today': today,
    }
    return render(request, "teacher/list.html", context)


def add_and_edit(request, pk=None):
    if pk:
        teacher = get_object_or_404(Teacher, id=pk)
    else:
        teacher = None
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
       
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
    form = TeacherForm(instance=teacher)
    context = {
        'form': form
    }
    return render(request, "teacher/forms.html", context)


# def edit(request, pk):
#     pass


def delete(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return redirect('teacher:index')
