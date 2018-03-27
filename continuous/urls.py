
from django.conf.urls import url,include
from .views import (
                    Continuous_AssessmentListView,
                    Continuous_AssessmentDetailView,
                    Continuous_AssessmentCreateView,
                    Continuous_AssessmentUpdateView
                    )
    

urlpatterns = [
    
        
    
    url(r'^(?P<pk>\d+)/update$',Continuous_AssessmentUpdateView.as_view(),name="update"), 
    url(r'^$', Continuous_AssessmentListView.as_view(),name="listcontinuous"),
    url(r'^create/$',Continuous_AssessmentCreateView.as_view(),name="addcontinuous"),
    url(r'^(?P<pk>\d+)/$',Continuous_AssessmentDetailView.as_view(),name="detail")
    
    
]
