from django.urls import path,include
from .views import login_user_index,login_user,logout_user

urlpatterns = [ 

path('',login_user_index,name="login_index"),
path("login",login_user,name="login"),
path("logout",logout_user,name="logout"),


]