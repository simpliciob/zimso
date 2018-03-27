from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Continuous_AssessmentForm
from .models import Continuous_Assessment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html",{})
        user=request.user
        
        is_following_user_ids=[x.user.id for x in user.is_following.all()]
        qs=Continuous_Assessment.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        for x in user.is_following.all():
            return render(request, "continuous/home-feed.html",{"object_list":qs})

class Continuous_AssessmentListView(ListView):
    def get_queryset(self):
        return Continuous_Assessment.objects.filter(user=self.request.user)
    
class Continuous_AssessmentDetailView(DetailView):
    def get_queryset(self):
        return Continuous_Assessment.objects.filter(user=self.request.user)
    

class Continuous_AssessmentCreateView(LoginRequiredMixin,CreateView):
    template_name="continuous/forms.html"
    form_class=Continuous_AssessmentForm
    def get_queryset(self):
        return Continuous_Assessment.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(Continuous_AssessmentCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add coursework'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(Continuous_AssessmentCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(Continuous_AssessmentCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class Continuous_AssessmentUpdateView(LoginRequiredMixin,UpdateView):
    template_name="continuous/detail-update.html"
    form_class=Continuous_AssessmentForm
    def get_queryset(self):
        return Continuous_Assessment.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(Continuous_AssessmentUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update continuous assessment'
        return context
    def get_form_kwargs(self):
        kwargs=super(Continuous_AssessmentUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


# Create your views here.


# Create your views here.
