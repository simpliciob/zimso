
from django.conf.urls import url,include
from .views import (ExamMarkListView,
                    ExamMarkCreateView,
                    ExamMarkDetailView,
                    ExamMarkUpdateView,
                    
                    )
    

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$',ExamMarkDetailView.as_view(),name="exams-detail"),
    url(r'^list/$', ExamMarkListView.as_view(),name="examlist"),
    url(r'^create/$',ExamMarkCreateView.as_view(),name="addmark"),
    url(r'^(?P<pk>\d+)/$',ExamMarkUpdateView.as_view(),name="updatem"),
    url(r'^(?P<pk>\d+)/update/$',ExamMarkUpdateView.as_view(),name="update"), 
    
    
    
]
