from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from JobApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='home' ),
    path('contact/', Contact, name='contact' ),
    path('student_login/', Student_Login, name='student_login' ),
    path('student_logout/', Student_Logout, name='student_logout' ),
    path('student_register/', Student_Register, name='student_register' ),
    path('student_home/', Student_Home, name='student_home' ),
    path('student_list/', Student_List, name='student_list' ),
    path('student_profile/', Student_Profile, name='student_profile' ),

    path('recruiter_login/', Recruiter_Login, name='recruiter_login'),
    path('recruiter_logout/', Recruiter_Logout, name='recruiter_logout' ),
    path('recruiter_register/', Recruiter_Register, name='recruiter_register'),
    path('recruiter_home/', Recruiter_Home, name='recruiter_home'),
    path('recruiter_profile/', Recruiter_Profile, name='recruiter_profile' ),
    
    path('admin_login/', Admin_Login, name='admin_login' ),
    path('admin_logout/', Admin_Logout, name='admin_logout' ),
    path('admin_home/', Admin_Home, name='admin_home' ),

    path('student_change_password/', Student_Change_Password, name='student_change_password'),
    path('recruiter_change_password/', Recruiter_Change_Password, name='recruiter_change_password'),
    path('change_password/', Change_Password, name='change_password'),

    path('view_students/',View_Students,name='view_students'),
    path('add_student/',Add_Student,name='add_student'),
    path('delete_student/<int:sid>',Delete_Student, name='delete_student'),
    
    path('change_status/<int:rid>',Change_Status,name='change_status'),
    path('pending_recruiters/',Pending_Recruiters,name='pending_recruiters'),
    path('accepted_recruiters/',Accepted_Rcruiters,name='accepted_recruiters'),
    path('rejected_recruiters/',Rejected_Recruiters,name='rejected_recruiters'),
    path('view_recruiters/',View_Recruiters,name='view_recruiters'),
    path('add_recruiter/',Add_Recruiter,name='add_recruiter'),
    path('delete_recruiter/<int:rid>', Delete_Recruiter, name='delete_recruiter'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

