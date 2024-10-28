from django.contrib import admin
from .models import School,Principal,Department,Course,Classes,Teacher,Student,Section
# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','number','address','city']

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ['id','name','school']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','section']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['id','name','section','school']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','classes','email','date_of_birth','phone','course','city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll_no','date_of_birth','classes','course','city']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','name']