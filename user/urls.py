
from django.contrib import admin
from django.urls import path
from .views import UserEditView
from .import views
from django.contrib.auth import views as auth_views

app_name='user'
urlpatterns = [
    path('login', views.loginform, name='login'),
    path('register', views.registeruser, name='registeruser'),
    path('', views.home, name='home' ),
    path('checkuser',views.check_username_exist, name='checkuser'),
    path('checkemail',views.check_email, name='checkemail'),
    path('checkemail',views.check_email, name='checkemail'),
    path('userdetails',views.checkdetails, name='checkdetails'),
    # path('edit_profile', views.UserEditView.as_view(), name='edit_profile'),
    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout',views.logout_request, name='logout'),
    path('additem', views.additem, name='additem'),
    path('viewitems', views.viewitems, name='viewitems'),
    path('interested/<str:pk>',  views.interested, name="interested")
]
