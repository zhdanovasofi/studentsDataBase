import uuid
from django.db import models

class Subject(models.Model):
    id_of_subject = models.AutoField(primary_key=True)
    name_of_subject= models.CharField(max_length=50,help_text="Subject is")
    id_tutor=models.ForeignKey('Tutor',  models.SET_NULL, blank=True, null=True,)
    def __str__(self):
        return self.name_of_subject

class Student(models.Model):
    students_ticket = models.AutoField(primary_key=True)
    FIO = models.CharField(max_length=30, help_text="Enter name of student")
    contacts = models.EmailField(max_length=254)
    intrance_year = models.IntegerField(default=2005, blank=True, null=True)
    subject = models.ManyToManyField(Subject)
    def get_course(self):
        import datetime
        return int(datetime.date.today().year) - self.intrance_year
    def __str__(self):
        return '%s %s' % (self.students_ticket,self.FIO)
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Tutor(models.Model):
    id_tutor= models.AutoField(primary_key=True)
    FIO = models.CharField(max_length=30, help_text="Enter name of the tutor")
    degree = models.CharField(max_length=30, help_text="Enter a degree of the tutor", blank=True, null=True)
    contacts = models.EmailField(max_length=254)
    def __str__(self):
        return self.FIO


class Grade_for_subject(models.Model):
    id_grade= models.AutoField(primary_key=True)
    semestre_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )
    semestre = models.IntegerField(choices=semestre_choices)
    students_id= models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    grade_choices = (
        (2, 'Не сдан'),
        (3, 'Удовлетворительно'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
        (5, 'Зачет'),
        (2, 'Не зачет')
    )
    grade = models.IntegerField(choices = grade_choices)
    def __str__(self):
        return '%s %s %s' % (self.students_id,self.semestre,self.subject_id)
