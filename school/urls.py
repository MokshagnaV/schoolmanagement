from . import views
from django.urls import path


urlpatterns=[
    path('',views.student_signup, name='stu_signup'),
    path('stu_login', views.student_login, name='stu_login'),
    path('home-page', views.home, name='student_home_page'),
    path('buddy-signup',views.buddy_signup, name='buddy_signup'),
    path('buddy-login', views.buddy_login, name='buddy_login'),
    path('buddy-home', views.buddy_home, name='buddy_home_page'),
    path('admin-signup',views.school_admin_signup, name='schooladmin_signup'),
    path('admin-login', views.school_admin_login, name='schooladmin_login'),
    path('admin-home', views.schooladmin_home, name='schooladmin')
]