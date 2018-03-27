from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
from eschool.models import Student
User=settings.AUTH_USER_MODEL
class Continuous_AssessmentQuerySet(models.query.QuerySet):
    def search(self,query):
        if query:
            query=query.strip()
            return self.filter(Q(student_number__icontains=query)
                               ).distinct()
        return self
class Continuous_AssessmentManager(models.Manager):
    def get_queryset(self):
        return Continuous_AssessmentQuerySet(self.model,using=self._db)
        
    def search(self,query):
        return self.get_queryset().search(query)

class Continuous_Assessment(models.Model):
    user=models.ForeignKey(User)
    student_number=models.ForeignKey(Student)
    subject_name=models.CharField(max_length=50)
    Total_Mark=models.IntegerField(null=True)
    comment=models.TextField(max_length=200,null=True)
    slug=models.SlugField(null=True, blank=True)
    name=models.CharField(max_length=200,default="simplicio")
    surname=models.CharField(max_length=40,default="sithole")
    Test_name=models.CharField(max_length=50)
    Test_mark=models.IntegerField(null=True)
    objects=Continuous_AssessmentManager()
    def __str__(self):
        return self.student_number


    def get_absolute_url(self):
        return reverse('continuous:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('continuous:update', kwargs={'pk':self.pk})
    


   

    
# Create your models here.



# Create your models here.
