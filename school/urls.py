
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from profiles.views import ProfileFollowToggle, RegisterView,activate_user_view
from teachers.views import HomeView
from django.views.generic import TemplateView
from eschool import views as eschool_views



urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',HomeView.as_view(),name="home"),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'),name="about"),
    url(r'^$',LoginView.as_view(), name="login"),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name="contact"),
    url(r'^exams/', include('teachers.urls',namespace="teachers")),
    url(r'^attendance/', include('attendance.urls',namespace="attendance")),
    url(r'^continuous/', include('continuous.urls',namespace="continuous")),
    url(r'^students/', include('students.urls',namespace="students")),
    url(r'^logout/$',LogoutView.as_view(), name="logout"),
    url(r'^activate/(?P<code>[a-z0-9].*)/$',activate_user_view, name='activate'),
    url(r'^register/$',RegisterView.as_view(), name="register"),
    url(r'^profile-follow/$',ProfileFollowToggle.as_view(),name="follow"),
    url(r'^u/', include('profiles.urls',namespace="profiles")),
    
    
    
]
