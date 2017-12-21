from django.conf.urls import url
from . import views
#this will help identify to which app the url is associated
app_name = 'login'

urlpatterns = [
    url(r'^$', views.homeView, name='HomeView'),
    url(r'^login/$', views.loginView, name='LoginView'),
    url(r'^logout/$', views.logoutView, name='LogoutView'),
]
