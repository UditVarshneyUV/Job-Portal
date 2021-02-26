from JobApp.models import RecruiterUser, StudentUser
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def Index(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'contact.html')

def Student_Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                u = StudentUser.objects.get(user=user)
                if u.type == "STUDENT":
                    login(request,user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    return render(request, 'student_login.html', {'error':error})

def Student_Logout(request):
    logout(request)
    return redirect('student_login')

def Student_Register(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        g = request.POST['gender']
        img = request.FILES['image']
        try:
            if not User.objects.filter(username=e).exists():
                user = User.objects.create_user(first_name=f, last_name=l,username=e, password=p)
                StudentUser.objects.create(user=user, gender=g, mobile=c,  image=img, type="STUDENT")
                error = "no"
            else:
                error = "user exists"
        except:
            error = "yes"         
    d = {'error':error}
    return render(request, 'student_register.html', d)

def Student_Home(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    return render(request, 'student_home.html')

def Student_List(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    return render(request, 'student_list.html')

def Student_Profile(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    user = User.objects.get(id = request.user.id)
    student = StudentUser.objects.filter(user = user).first()
    print(student)
    d = {'student':student}
    return render(request, 'student_profile.html',d)

def Student_Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['curr_pwd']
        n = request.POST['new_pwd']
        if n != "":
            try:
                u = User.objects.get(id = request.user.id)
                if u.check_password(c):
                    u.set_password(n)
                    u.save()
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "empty"    
    e = {'error':error}
    return render(request, 'student_change_password.html',e)

def Recruiter_Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                r = RecruiterUser.objects.get(user=user)
                if r.type == "RECRUITER" and r.status == "accepted":
                    login(request,user)
                    error = "no"
                elif r.type == 'RECRUITER' and r.status == "rejected":
                    error = "rejected"
                elif r.type == "RECRUITER" and r.status == "pending":
                    error = "pending"
            except:
                error = "yes"
        else:
            error = "yes"
    return render(request, 'recruiter_login.html',{'error':error})

def Recruiter_Logout(request):
    logout(request)
    return redirect('recruiter_login')

def Recruiter_Register(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        cm = request.POST['company']
        p = request.POST['pwd']
        g = request.POST['gender']
        img = request.FILES['image']

        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            RecruiterUser.objects.create(user=user, gender=g, mobile=c, company=cm, image=img, type="RECRUITER",status="pending")
            error = "no"
        except:
            error = "yes"   
    d = {'error':error}
    return render(request, 'recruiter_register.html', d)

def Recruiter_Home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, 'recruiter_home.html')

def Recruiter_Profile(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = User.objects.get(id = request.user.id)
    recruiter = RecruiterUser.objects.filter(user = user).first()
    print(recruiter)
    d = {'recruiter':recruiter}
    return render(request, 'recruiter_profile.html',d)

def Recruiter_Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['curr_pwd']
        n = request.POST['new_pwd']
        if n != "":
            try:
                u = User.objects.get(id = request.user.id)
                if u.check_password(c):
                    u.set_password(n)
                    u.save()
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "empty"
    
    e = {'error':error}
    return render(request, 'recruiter_change_password.html',e)

def Admin_Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html',{'error':error})

def Admin_Logout(request):
    logout(request)
    return redirect('admin_login')

def Admin_Home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    students = StudentUser.objects.all()
    recruiters = RecruiterUser.objects.all()
    pending_recruiters = RecruiterUser.objects.filter(status='pending')
    accepted_recruiters = RecruiterUser.objects.filter(status='accepted')
    rejected_recruiters = RecruiterUser.objects.filter(status='rejected')
    s = len(students)
    r = len(recruiters)
    p = len(pending_recruiters)
    a = len(accepted_recruiters)
    rj = len(rejected_recruiters)
    d = {'students':s,'recruiters':r,'pending_recruiters':p,'accepted_recruiters':a,'rejected_recruiters':rj}
    return render(request, 'admin_home.html',d)

def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['curr_pwd']
        n = request.POST['new_pwd']
        if n != "":
            try:
                u = User.objects.get(id = request.user.id)
                if u.is_staff and u.check_password(c):
                    u.set_password(n)
                    u.save()
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "empty"
    
    e = {'error':error}
    return render(request, 'change_password.html',e)

def View_Students(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    students = StudentUser.objects.all()
    s = {'students':students}
    return render(request, 'view_students.html',s)

def Delete_Student(request,sid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = StudentUser.objects.get(id = sid)
    user = User.objects.get(username=student.user.username)
    user.delete()
    student.delete()
    return redirect('view_students')

def Add_Student(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        g = request.POST['gender']
        img = request.FILES['image']

        try:
            if not User.objects.filter(username=e).exists():
                user = User.objects.create_user(first_name=f, last_name=l,username=e, password=p)
                StudentUser.objects.create(user=user, gender=g, mobile=c,  image=img, type="STUDENT")
                error = "no"
            else:
                error = "user exists"
        except:
            error = "yes"
         
    d = {'error':error}
    return render(request, 'add_student.html', d)

def Pending_Recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    pending_recruiters = RecruiterUser.objects.filter(status='pending')
    p = {'pending_recruiters':pending_recruiters}
    return render(request, 'pending_recruiters.html', p)

def Accepted_Rcruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    accepted_recruiters = RecruiterUser.objects.filter(status='accepted')
    p = {'accepted_recruiters':accepted_recruiters}
    return render(request, 'accepted_recruiters.html', p)

def Rejected_Recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rejected_recruiters = RecruiterUser.objects.filter(status='rejected')
    p = {'rejected_recruiters':rejected_recruiters}
    return render(request, 'rejected_recruiters.html', p)

def Change_Status(request,rid):
    error = ""
    status = ""
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = RecruiterUser.objects.get(id = rid)
    if request.method == 'POST':
        s = request.POST['status']
        if not s == "":
            recruiter.status = s
            try:
                status = recruiter.status
                recruiter.save()
                error = "no"
            except:
                error = "yes"
        else:
            error = "not"
    p = {'recruiter':recruiter,'error':error,'status':status}
    return render(request,'change_status.html',p)

def View_Recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiters = RecruiterUser.objects.all()
    r = {'recruiters':recruiters}
    return render(request, 'view_recruiters.html', r)

def Add_Recruiter(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        cm = request.POST['company']
        p = request.POST['pwd']
        g = request.POST['gender']
        img = request.FILES['image']

        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            RecruiterUser.objects.create(user=user, gender=g, mobile=c, company=cm, image=img, type="RECRUITER",status="pending")
            error = "no"
        except:
            error = "yes"
         
    d = {'error':error}
    return render(request, 'add_recruiter.html', d)

def Delete_Recruiter(request,rid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = RecruiterUser.objects.get(id = rid)
    user = User.objects.get(username=recruiter.user.username)
    user.delete()
    recruiter.delete()
    return redirect('view_recruiters')