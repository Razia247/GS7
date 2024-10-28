from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Principal(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=50)
     
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
 
class Classes(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True,blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50)
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,)
    

    def __str__(self):
        return self.name




