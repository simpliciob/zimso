from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExamMarkForm
from .models import ExamMark
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        #if not request.user.is_authenticated():
        return render(request, "teachers/home.html",{})
        #user=request.user
        
        #is_following_user_ids=[x.user.id for x in user.is_following.all()]
        #qs=ExamMark.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        #for x in user.is_following.all():
            #return render(request, "teachers/home-feed.html",{"object_list":qs})

class ExamMarkListView(ListView):
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    
class ExamMarkDetailView(DetailView):
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    
    
class ExamMarkCreateView(LoginRequiredMixin,CreateView):
    form_class=ExamMarkForm
    login_url='/login/'
    template_name="teachers/forms.html"
    success_url="/"
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ExamMarkCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Exam Marks'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(ExamMarkCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(ExamMarkCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

    
    
class ExamMarkUpdateView(LoginRequiredMixin,UpdateView):
    template_name="teachers/detail-update.html"
    form_class=ExamMarkForm
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ExamMarkUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Exam Marks'
        return context
    def get_form_kwargs(self):
        kwargs=super(ExamMarkUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs




# Create your views here.
