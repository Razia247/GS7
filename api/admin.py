from django.contrib import admin
from .models import School,Principal,VicePrincipal,Course,Classes,Teacher,Student
# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name','city']

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ['id','name','school']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(VicePrincipal)
class VicePrincipalAdmin(admin.ModelAdmin):
    list_display = ['id','name','school']

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['id','name','school']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','classes','course','city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll_no','classes','course','city']
