from django.db import models
from django.db import models

class People (models.Model):
    
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    Phonenumber=models.CharField(max_length=10)
    Physical_Address=models.TextField(max_length=200)
    Email_Address=models.EmailField(max_length=254, null=True, blank=True)
    Image=models.FileField(upload_to='uploads/')
    DOB=models.DateField()
    class Meta:
        abstract=True
class Subject(models.Model):
    subject_name=models.CharField(max_length=20)
    subject_ID=models.CharField(max_length=20,primary_key=True,unique=True)
    def __str__(self):
        return self.subject_ID
class Teacher(People):
    
    EmploymentID=models.CharField(max_length=50, primary_key=True,unique=True)
    subject_ID=models.ForeignKey(Subject,on_delete=models.CASCADE)
    def __str__(self):
        return self.EmploymentID
class Student(People):
    student_number=models.CharField(max_length=50, primary_key=True,unique=True)
    def __str__(self):
        return self.student_number
    
class Parent(People):
    NID=models.CharField(max_length=50, unique=True)
    position=models.CharField(max_length=50)
    student_number=models.ManyToManyField(Student)
    landline_number=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    def __str__(self):
        return self.lastname

class Hostel(models.Model):
    hostel_ID=models.CharField(max_length=20,primary_key=True)
    hostel_name=models.CharField(max_length=20)
    student_number=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.hostel_ID
class Fee(models.Model):
    Amount_paid=models.DecimalField(max_digits=5, decimal_places=2)
    student_number=models.ForeignKey(Student,on_delete=models.CASCADE)
    invoice_number=models.CharField(max_length=50)
    tutoring_fee=models.DecimalField(max_digits=5, decimal_places=2)
    Bank_name=models.CharField(max_length=50)
class Book(models.Model):
    book_number=models.CharField(max_length=50,primary_key=True,unique=True)
    published_date=models.DateField()
    Author=models.CharField(max_length=50)
    book_title=models.CharField(max_length=50)
    def __str__(self):
        return self.book_number
class Borrowing(models.Model):
    book_number=models.CharField(max_length=50,primary_key=True)
    book_title=models.CharField(max_length=50)
    student_number=models.ForeignKey(Student,on_delete=models.CASCADE)
    date_taken=models.DateField()
    return_date=models.DateField()


   
                     

     
    

    
    

# Create your models here.


# Create your models here.
