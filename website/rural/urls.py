from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static

app_name = "rural"   


urlpatterns = [
   
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.loginpage, name="loginpage"),
    path('logout', views.logout_user, name= "logout_user"),
    path('birth',views.birth),
    path('death',views.death),
    

]
