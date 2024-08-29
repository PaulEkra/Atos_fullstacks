from student.models import Student
from teacher.models import Teacher
from user.models import User
def count(request):
    students=Student.objects.all()
    students_female=Student.objects.filter(gender=False).count()
    students_male=Student.objects.filter(gender=True).count()
    teachers=Teacher.objects.all()
    users=User.objects.all()
    student_number=students.count()
    teacher_number=teachers.count()
    user_number=users.count()
    
    return { 'total_students':student_number,
             'total_students_female':students_female,
             'total_students_male':students_male,
             'total_teachers':teacher_number,
             'total_users':user_number,
            }

