from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q

from eschool.models import Student
User=settings.AUTH_USER_MODEL

class Marks(models.Model):
    user=models.ForeignKey(User)
    student_number=models.ForeignKey(Student)
    subject_name=models.CharField(max_length=50)
    Total_Mark=models.IntegerField()
    comment=models.TextField(max_length=200)
    slug=models.SlugField(null=True, blank=True)
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=40)

class ExamMarkQuerySet(models.query.QuerySet):
    def search(self,query):
        if query:
            query=query.strip()
            return self.filter(Q(student_number__icontains=query)
                               ).distinct()
        return self
class ExamMarkManager(models.Manager):
    def get_queryset(self):
        return ExamMarkQuerySet(self.model,using=self._db)
        
    def search(self,query):
        return self.get_queryset().search(query)
    
    
   
class ExamMark(Marks):
    
    paper1_Mark=models.IntegerField(null=True,blank=True)
    paper2_Mark=models.IntegerField(null=True, blank=True)
    paper3_Mark=models.IntegerField(null=True, blank=True)
    paper4_Mark=models.IntegerField(null=True, blank=True)
    paper5_Mark=models.IntegerField(null=True, blank=True)
    paper6_Mark=models.IntegerField(null=True, blank=True)
    objects=ExamMarkManager()
    def __str__(self):
        return self.student_number


    def get_absolute_url(self):
        return reverse('teachers:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('teachers:update', kwargs={'pk':self.pk})


    
# Create your models here.
