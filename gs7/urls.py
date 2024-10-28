
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/',views.SchoolApi.as_view()),
    path('school/<int:pk>/',views.SchoolApi.as_view()),
    path('principal/',views.PrincipalApi.as_view()),
    path('principal/<int:pk>/',views.PrincipalApi.as_view()),
    path('course/',views.CourseApi.as_view()),
    path('course/<int:pk>/',views.CourseApi.as_view()),
    path('department/',views.DepartmentApi.as_view()),
    path('department/<int:pk>/',views.DepartmentApi.as_view()),
    path('classes/',views.ClassesApi.as_view()),
    path('classes/<int:pk>/',views.ClassesApi.as_view()),
    path('teacher/',views.TeacherApi.as_view()),
    path('teacher/<int:pk>/',views.TeacherApi.as_view()),
    path('student/',views.StudentApi.as_view()),
    path('student/<int:pk>/',views.StudentApi.as_view()),
    path('section/',views.SectionApi.as_view()),
    path('section/<int:pk>/',views.SectionApi.as_view()),
    
]
