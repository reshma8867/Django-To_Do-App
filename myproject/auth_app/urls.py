from django.urls import path
from auth_app import views

urlpatterns=[
    path('',views.login_,name='login_'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('logout_',views.logout_,name='logout_'),
    path('change_password',views.change_password,name='change_password'),
    path("update_profile/", views.update_profile, name="update_profile")
]