from rest_framework import serializers
from .models import School,Principal,Department,Course,Classes,Teacher,Student,Section

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','name','email','number','address','city']

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = ['id','name','school']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','section']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name',]

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id','name','school','section']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','classes','course','city','email','date_of_birth','phone']
                  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['id','name','roll_no','date_of_birth','classes','course','city']
class SectionSerializer(serializers.ModelField):
    class Meta:
        model = Section
        fields = ['id','name']