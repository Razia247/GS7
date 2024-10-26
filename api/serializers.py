from rest_framework import serializers
from .models import School,Principal,VicePrincipal,Course,Classes,Teacher,Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','name','city']

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = ['id','name','school']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name']

class VicePrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VicePrincipal
        fields = ['id','name','school']

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id','name','school']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','classes','course','city']
                  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll_no','classes','course','city']