from django.contrib import admin

from .models import Student,Subject,Grade_for_subject, Tutor
#admin.site.register(Student)
#admin.site.register(Subject)
#admin.site.register(Tutor)
#admin.site.register(Grade_for_subject)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('students_ticket','FIO' )
admin.site.register(Student, StudentAdmin)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name_of_subject', 'id_tutor')
admin.site.register(Subject, SubjectAdmin)
class TutorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tutor, TutorAdmin)
class Grade_for_subjectAdmin(admin.ModelAdmin):
    list_display = ('students_id', 'subject_id', 'grade')
admin.site.register(Grade_for_subject, Grade_for_subjectAdmin)
