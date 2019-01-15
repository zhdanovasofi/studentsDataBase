from django.shortcuts import render, redirect
from .models import Student,Subject,Grade_for_subject, Tutor
from django.views import generic
import datetime
from django.shortcuts import render_to_response

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    students_count=Student.objects.all().count()

    return render(
        request,
        'index.html',
        context={'Students in department ': students_count},
    )

class StudentsListView(generic.ListView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentsDetailView(generic.ListView):
    model = Grade_for_subject
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TutotListView(generic.ListView):
    model = Tutor
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def search_form(request):
   return render(request,'student_list.html')
def search(request):
    course = int(request.GET['course'])
    int_year  = int(datetime.date.today().year) - course
    students = Student.objects.filter(intrance_year = int_year).order_by('FIO')
    return render(request,'search_results.html',{'students': students, 'course': course })

def fio_search_form(request):
    return render(request,'student_search.html')

def fio_search(request):
    fio = request.GET['fio']
    student  = Student.objects.filter(FIO = fio).values('students_ticket').distinct()
    #studentID = student.students_ticket
    grades = Grade_for_subject.objects.filter(students_id__in=student)
    return render(request,'searchFIO_results.html',{'fio': fio, 'grades': grades })
