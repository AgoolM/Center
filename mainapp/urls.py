from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashbord,name='dashbord'),
    path('test/',views.base_page,name='base'),
    path('logistic-content-page/', views.logistic_content_page, name='logistic'),
    
    path('login/',views.login_user,name='login'),
    path('register/',views.register_user, name='register'),
    path('logout/',views.logout_user, name='logout'),
    
    path('course-c/',views.course_cerate, name='course_c'),
    path('course-t/', views.course_table, name="course_t"),
    path('course_u/<int:pk>', views.update_course, name='course_u'),
    path('course_d/<int:pk>', views.delete_course, name='course_d'),

    path('group-c/',views.group_cerate, name='group_c'),
    path('group-t/', views.group_table, name="group_t"),
    path('group_u/<int:pk>', views.update_group, name='group_u'),
    path('group_d/<int:pk>', views.delete_group, name='group_d'),

    path('mentor-c/',views. mentor_create, name='mentor_c'),
    path('mentor-t/', views.mentor_table, name="mentor_t"),
    path('mentor_u/<int:pk>', views.update_mentor, name='mentor_u'),
    path('mentor_d/<int:pk>', views.delete_mentor, name='mentor_d'),

    path('mentee-c/',views.mentee_create, name='mentee_c'),
    path('mentee-t/', views.mantee_table, name="mentee_t"),
    path('mentee_u/<int:pk>', views.update_mentee, name='mentee_u'),
    path('mentee_d/<int:pk>', views.delete_mentee, name='mentee_d'),

    path('video-c/',views.video_cerate, name='video_c'),
    path('video-u/<int:pk>', views.update_video, name='video_u'),
    path('video-d/<int:pk>', views.delete_video, name='video_d'),
]