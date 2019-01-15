from django.conf.urls import url
from . import views
from django.urls import path,re_path
from catalog.views import StudentsListView,TutotListView, StudentsDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.search_form, name='students'),
    path('student/search/', views.search),
    path('tutor/', TutotListView.as_view(), name = 'tutor'),
    path('grade/', views.fio_search_form, name = 'grade'),
    path('grade/fio_search/', views.fio_search),
]
