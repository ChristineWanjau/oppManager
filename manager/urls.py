from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.logged,name="home"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('postjob/',views.postJob,name="postjob"),
    path('newaccount/',views.newAccount,name="newaccount"),
    path('displayJob/<jobid>/',views.displayJob,name="displayjob"),
    path('displayCompany/<companyid>/',views.displayCompany,name="displaycompany")
    


]


    