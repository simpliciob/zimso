from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from teachers.models import ExamMark
from continuous.models import Continuous_Assessment
from eschool.models import Student, Borrowing,Hostel,Fee
from attendance.models import Attendance
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View
from django.contrib.auth.models import User

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html",{})
        user=request.user
        
        is_following_user_ids=[x.user.id for x in user.is_following.all()]
        qs=Continuous_Assessment.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        for x in user.is_following.all():
            return render(request, "continuous/home-feed.html",{"object_list":qs})
    
    

#class Continuous_AssessmentListView(LoginRequiredMixin,ListView):
   
  # template_name="students/continuous_assessment_list.html"
   #model=Continuous_Assessment
   
   #def get_context_data(self,*args,**kwargs):
        #user=self.request.user
        
        #taken=super(Continuous_AssessmentListView, self).get_context_data(*args,**kwargs)
        #taken['locations'] =Continuous_Assessment.objects.filter(student_number=user)
        #return taken
class Continuous_AssessmentListView(ListView):
    template_name="students/continuous_list.html"
    context_object_name = 'continuous_list'
    def get_queryset(self):
        user=self.request.user
        return Continuous_Assessment.objects.filter(student_number__student_number=user)
class AttendanceListView(ListView):
    template_name="students/attendance_List.html"
    context_object_name = 'attendance_list'
    def get_queryset(self):
        user=self.request.user
        return Attendance.objects.filter(student_number__student_number=user)

class ExamMarkListView(ListView):
    template_name="students/exammark_list.html"
    context_object_name = 'exammark_list'
    def get_queryset(self):
        user=self.request.user
        return ExamMark.objects.filter(student_number__student_number=user)
class FeeListView(ListView):
    template_name="students/fee_list.html"
    context_object_name = 'fee_list'
    def get_queryset(self):
        user=self.request.user
        return Fee.objects.filter(student_number__student_number=user)
class BorrowingListView(ListView):
    template_name="students/borrow_list.html"
    context_object_name = 'borrow_list'
    def get_queryset(self):
        user=self.request.user
        return Borrowing.objects.filter(student_number__student_number=user)
class HostelListView(ListView):
    template_name="students/hostel_list.html"
    context_object_name = 'hostel_list'
    def get_queryset(self):
        user=self.request.user
        return Hostel.objects.filter(student_number__student_number=user)



    
    


    
   # def get_queryset(self):
        #user=self.request.user
        #return Continuous_Assessment.objects.filter(Q(student_number__iexact=user)|
                                                    #Q(user=self.request.user))
    
    
        
        
  
        
    


# Create your views here.


# Create your views here.
