from django.shortcuts import render, redirect
from .models import student, buddy, school_admin
from django.contrib import messages

# Create your views here.


def student_signup(request):
    if request.method=='POST':
        form = request.POST['submit']
        if form=='Submit':
            entered_id=request.POST['stu_id']
            entered_name=request.POST['stu_name']
            entered_fname=request.POST['fname']
            entered_gender=request.POST['gender']
            entered_email = request.POST['email']
            entered_pwd=request.POST['password']
            entered_dob= request.POST['dob']
            entered_school = request.POST['school']
            entered_class = request.POST['pre_class']
            entered_mobile = request.POST['mobile']
            #entered_image = request.FILES['stu_photo']

            student_details= student(
                stu_id = entered_id,
                stu_name = entered_name,
                fname = entered_fname,
                gender = entered_gender,
                email = entered_email,
                pwd = entered_pwd,
                dob = entered_dob, 
                school = entered_school,
                present_class = entered_class,
                mobile = entered_mobile
                #photo = entered_image
            )

            student_details.save()

            return redirect('stu_login')
        else:
            print("hii")

    return render(request, 'school/student_singup.html')

def student_login(request):
    if request.method=='POST':
        form=request.POST['submit']
        if form=="Submit":
            username = request.POST['username']
            password = request.POST['password']

            details = student.objects.get(email = username)

            if password== details.pwd:
                return redirect('student_home_page')
            else:
                messages.info(request, 'Invalid Username or Password')

    return render(request, 'school/student_login.html')


def home(request):
    return render(request, 'school/student_home.html')

#--------------------------------------


def buddy_signup(request):
    if request.method=='POST':
        form = request.POST['submit']
        if form=='Submit':
            entered_id=request.POST['buddy_id']
            entered_name=request.POST['buddy_name']
            entered_fname=request.POST['fname']
            entered_gender=request.POST['gender']
            entered_email = request.POST['email']
            entered_pwd=request.POST['password']
            entered_dob= request.POST['dob']
            entered_designation = request.POST['designation']
            entered_workplace = request.POST['workplace']
            entered_mobile = request.POST['mobile']
            #entered_image = request.FILES['stu_photo']

            buddy_details= buddy(
                buddy_id = entered_id,
                buddy_name = entered_name,
                fname = entered_fname,
                gender = entered_gender,
                email = entered_email,
                pwd = entered_pwd,
                dob = entered_dob, 
                designation = entered_designation,
                workplace = entered_workplace,
                mobile = entered_mobile
                #photo = entered_image
            )

            buddy_details.save()

            return redirect('buddy_login')
        else:
            print("hii")

    return render(request, 'school/buddy_singup.html')

def buddy_login(request):
    if request.method=='POST':
        form=request.POST['submit']
        if form=="Submit":
            username = request.POST['username']
            password = request.POST['password']

            details = buddy.objects.get(email = username)

            if password== details.pwd:
                return redirect('buddy_home_page')
            else:
                messages.info(request, 'Invalid Username or Password')

    return render(request, 'school/buddy_login.html')


def buddy_home(request):
    return render(request, 'school/buddy_home.html')

#----------------------------------------------------


def school_admin_signup(request):
    if request.method=='POST':
        form = request.POST['submit']
        if form=='Submit':
            entered_id=request.POST['schooladmin_id']
            entered_name=request.POST['schooladmin_name']
            entered_schoolid = request.POST['school_id']
            entered_schoolname = request.POST['school_name']
            entered_fname=request.POST['fname']
            entered_gender=request.POST['gender']
            entered_email = request.POST['email']
            entered_pwd=request.POST['password']
            entered_dob= request.POST['dob']
            entered_designation = request.POST['designation']
            entered_mobile = request.POST['mobile']
            #entered_image = request.FILES['stu_photo']

            admin_details= school_admin(
                school_admin_id = entered_id,
                school_admin_name = entered_name,
                school_id = entered_schoolid,
                school_name = entered_schoolname,
                fname = entered_fname,
                gender = entered_gender,
                email = entered_email,
                pwd = entered_pwd,
                dob = entered_dob,
                designation = entered_designation,
                mobile = entered_mobile,
                #photo = entered_image
            )

            admin_details.save()

            return redirect('schooladmin_login')
        else:
            print("hii")

    return render(request, 'school/school_admin_singup.html')

def school_admin_login(request):
    if request.method=='POST':
        form=request.POST['submit']
        if form=="Submit":
            username = request.POST['username']
            password = request.POST['password']

            details = school_admin.objects.get(email = username)

            if password== details.pwd:
                return redirect('schooladmin')
            else:
                messages.info(request, 'Invalid Username or Password')

    return render(request, 'school/school_admin_login.html')


def schooladmin_home(request):
    return render(request, 'school/school_admin.html')