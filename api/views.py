from django.shortcuts import render
from .models import School,Principal,VicePrincipal,Course,Classes,Teacher,Student
from .serializers import SchoolSerializer,PrincipalSerializer,VicePrincipalSerializer,CourseSerializer,ClassesSerializer,TeacherSerializer,StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SchoolApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = School.objects.get(id=id)
            serializer = SchoolSerializer(info)
            return Response(serializer.data)
        info = School.objects.all()
        serializer = SchoolSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = School.objects.get(id=id)
        serializer = SchoolSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = School.objects.get(id=id)
        serializer = SchoolSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = School.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    
class PrincipalApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = Principal.objects.get(id=id)
            serializer = PrincipalSerializer(info)
            return Response(serializer.data)
        info = Principal.objects.all()
        serializer = PrincipalSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PrincipalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Principal.objects.get(id=id)
        serializer = PrincipalSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Principal.objects.get(id=id)
        serializer = PrincipalSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Principal.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    
class CourseApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = Course.objects.get(id=id)
            serializer = CourseSerializer(info)
            return Response(serializer.data)
        info = Course.objects.all()
        serializer = CourseSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Course.objects.get(id=id)
        serializer = CourseSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Course.objects.get(id=id)
        serializer = CourseSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Course.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    
class VicePrincipalApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = VicePrincipal.objects.get(id=id)
            serializer = VicePrincipalSerializer(info)
            return Response(serializer.data)
        info = VicePrincipal.objects.all()
        serializer = VicePrincipalSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = VicePrincipalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = VicePrincipal.objects.get(id=id)
        serializer = VicePrincipalSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = VicePrincipal.objects.get(id=id)
        serializer = VicePrincipalSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = VicePrincipal.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    
class ClassesApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = Classes.objects.get(id=id)
            serializer = ClassesSerializer(info)
            return Response(serializer.data)
        info = Classes.objects.all()
        serializer = ClassesSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Classes.objects.get(id=id)
        serializer = ClassesSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Classes.objects.get(id=id)
        serializer = ClassesSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Classes.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    
class TeacherApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(info)
            return Response(serializer.data)
        info = Teacher.objects.all()
        serializer = TeacherSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Teacher.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    
class StudentApi(APIView):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        if id is not None:
            info = Student.objects.get(id=id)
            serializer = StudentSerializer(info)
            return Response(serializer.data)
        info = Student.objects.all()
        serializer = StudentSerializer(info,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Student.objects.get(id=id)
        serializer = StudentSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data completely updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Student.objects.get(id=id)
        serializer = StudentSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk',None)
        info = Student.objects.get(id=id)
        info.delete()
        return Response({'msg':'Data successfully deleted'})
    