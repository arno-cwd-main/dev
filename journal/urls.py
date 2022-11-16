
from django.urls import path

from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [

    # - Homepage

    path('', views.home, name=""),
    

    # - Register

    path('register', views.register, name="register"),


    # - Login 

    path('my-login', views.my_login, name="my-login"),




    # - Dashboard 

    path('dashboard', views.dashboard, name="dashboard"),


    # - Post thought

    path('post-thought', views.post_thought, name="post-thought"),


    # - My thoughts

    path('my-thoughts', views.my_thoughts, name="my-thoughts"),


    # - Update-thought

    path('update-thought/<str:pk>', views.update_thought, name="update-thought"),


    # - Delete thought

    path('delete-thought/<str:pk>', views.delete_thought, name="delete-thought"),




    # - Profile management

    path('profile-management', views.profile_management, name="profile-management"),



    # - Delete account

    path('delete-account', views.delete_account, name="delete-account"),




    # - Logout url

    path('user-logout', views.user_logout, name="user-logout"),




    # 1 - Allows us to enter our email in order to receive a password reset link

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password-reset/password-reset.html"), name='reset_password'),


    # 2 - Show a success message stating that an email was sent to reset our password 

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password-reset/password-reset-sent.html"), name='password_reset_done'),


    # 3 - Send a link to our email, so that we can reset our password

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset/password-reset-form.html"), name='password_reset_confirm'),


    # 4 - Show message stating that our password was changed

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset/password-reset-complete.html"), name='password_reset_complete'),


















]






