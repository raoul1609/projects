from django.urls import path 
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('save/', views.saveProgram, name='saveProgram'),
    path('view/', views.getProgram, name='showProgram'),
    path('save/teacher/', views.addTeacher, name="addTeacher"),
    path('view/<str:name>', views.lookForOneProgram, name="searchProgram"),

    ## LIENS POUR ACCES AUX APIS ##
    path('api/teachers/', views.MiawTeachersList.as_view()),
    path('api/teacher/<str:pk>', views.MiawTeachersDetail.as_view())
]