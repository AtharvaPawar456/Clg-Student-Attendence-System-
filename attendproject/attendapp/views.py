#  i have created this file - GTA
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TeacherData, Studentprofile, Studattendence, TimeTable
# import uuid
import random
from random import choice
from django.db import IntegrityError

import ast
from datetime import timedelta
# from datetime import date
from django.utils import timezone
import datetime

# gemini imports
# import google.generativeai as genai
# import json
# import base64
# import pathlib
# import pprint
# import requests
# import mimetypes
# from IPython.display import Markdown

# API_KEY="AIzaSyD9ZF_AshNR1jYQSxdSaEED7gboME_X9_M"
# genai.configure(api_key=API_KEY)
# model = 'gemini-1.0-pro' # @param {isTemplate: true}
# contents_b64 = 'W10='
# generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119'
# safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d'




# You can use the ast module in Python to safely convert a string representation of a list to an actual list. Here's how you can do it:

# from django.http import HttpResponse
# from .models import Product, Contact

# Create your views here.

# Login / Register / Logout


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        phoneno  = request.POST['phoneno']
        address  = request.POST['address']
        password = request.POST['password']
        email    = request.POST['email']

        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            TeacherData_data = TeacherData(name=username, phoneno=phoneno, emailid= email, address=address)
            TeacherData_data.save() # Save the instance to the database
            
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None
    return render(request, 'attendapp/register.html', {'error_message': error_message})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'attendapp/login.html',
                  {'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view




def welcome(request):
    return render(request, 'attendapp/welcome.html')

'''
    year   = models.IntegerField(default=2024)
    rollno = models.IntegerField(default=0)
    name   = models.CharField(max_length=200, default="-")
    div    = models.CharField(max_length=200, default="-")
    branch = models.CharField(max_length=200, default="-")
    y1cgpa = models.FloatField(verbose_name='Y1CGPA', default=0.0)
    y1sgpa = models.FloatField(verbose_name='Y1SGPA', default=0.0)   
    address = models.CharField(max_length=1000, default="-")
    phoneno = models.CharField(max_length=200, default="-")
    parentphoneno = models.CharField(max_length=200, default="-")
    teachername = models.CharField(max_length=200, default="Sahil")
'''

def addstudent(request):
    if request.method == 'POST':
        year = request.POST['year']
        rollno = request.POST['rollno']
        username = request.POST['username']
        div = request.POST['div']
        branch = request.POST['branch']
        parentphoneno = request.POST['parentphoneno']
        phoneno  = request.POST['phoneno']
        address  = request.POST['address']
        y1cgpa  = request.POST['y1cgpa']
        y1sgpa  = request.POST['y1sgpa']

        print("Year:", year)
        print("Roll No:", rollno)
        print("Username:", username)
        print("Division:", div)
        print("Branch:", branch)
        print("Parent Phone No:", parentphoneno)
        print("Phone No:", phoneno)
        print("Address:", address)
        print("Y1 CGPA:", y1cgpa)
        print("Y1 SGPA:", y1sgpa)

        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            TeacherData_data = Studentprofile(year=int(year), rollno=int(rollno), name=username, div=div, branch=branch, phoneno=phoneno, parentphoneno= parentphoneno, address=address, y1cgpa=y1cgpa, y1sgpa=y1sgpa)
            TeacherData_data.save() # Save the instance to the database
            
            return redirect('dashboard')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None
    return render(request, 'attendapp/addstudent.html', {'error_message': error_message})

'''
    branch         = models.CharField(max_length=200, default="-")
    year         = models.CharField(max_length=200, default="-")
    div         = models.CharField(max_length=200, default="-")
    day         = models.CharField(max_length=200, default="-")
    starttime   = models.CharField(max_length=200, default="-")
    endtime     = models.CharField(max_length=200, default="-")
    leacture    = models.CharField(max_length=200, default="-") #subject
    lectProf    = models.CharField(max_length=200, default="-")
    status      = models.CharField(max_length=200, default="present")
'''


def addtimetable(request):
    if request.method == 'POST':
        branch = request.POST['branch']
        year = request.POST['year']
        div = request.POST['div']
        day = request.POST['day']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        leacture = request.POST['leacture']
        lectProf = request.POST['lectProf']
        status = "present"
        
        

        print("Branch:", branch)
        print("Year:", year)
        print("Division:", div)
        print("day:", day)
        print("starttime:", starttime)
        print("endtime:", endtime)
        print("leacture:", leacture)
        print("lectProf:", lectProf)
        print("status:", status)



        # Check if the username is unique
        # if not User.objects.filter(username=username).exists():
            # Create a new user
        TimeTable_data = TimeTable(branch=branch, year=year, div=div, day=day, starttime=starttime , endtime=endtime, leacture= leacture, lectProf=lectProf, status=status)
        TimeTable_data.save() # Save the instance to the database
            
        return redirect('dashboard')  # Redirect to your login view
        # else:
        #     error_message = 'Username already exists'
    else:
        error_message = None
    return render(request, 'attendapp/addtimetable.html', {'error_message': error_message})










def databaseupdate(request):
    # Create timetable entries
    timetable_data = [
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Monday", 'starttime': '09:00', 'endtime': '10:30', 'leacture': 'Maths', 'lectProf': 'Dr. Smith'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Monday", 'starttime': '11:00', 'endtime': '12:30', 'leacture': 'Physics', 'lectProf': 'Prof. Johnson'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Monday", 'starttime': '13:00', 'endtime': '14:00', 'leacture': 'Science', 'lectProf': 'Prof. Johnny'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Monday", 'starttime': '14:00', 'endtime': '15:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Monday", 'starttime': '15:00', 'endtime': '16:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},

        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Tuesday", 'starttime': '09:00', 'endtime': '10:30', 'leacture': 'Maths', 'lectProf': 'Dr. Smith'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Tuesday", 'starttime': '11:00', 'endtime': '12:30', 'leacture': 'Physics', 'lectProf': 'Prof. Johnson'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Tuesday", 'starttime': '13:00', 'endtime': '14:00', 'leacture': 'Science', 'lectProf': 'Prof. Johnny'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Tuesday", 'starttime': '14:00', 'endtime': '15:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Tuesday", 'starttime': '15:00', 'endtime': '16:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},

        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Wednesday", 'starttime': '09:00', 'endtime': '10:30', 'leacture': 'Maths', 'lectProf': 'Dr. Smith'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Wednesday", 'starttime': '11:00', 'endtime': '12:30', 'leacture': 'Physics', 'lectProf': 'Prof. Johnson'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Wednesday", 'starttime': '13:00', 'endtime': '14:00', 'leacture': 'Science', 'lectProf': 'Prof. Johnny'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Wednesday", 'starttime': '14:00', 'endtime': '15:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Wednesday", 'starttime': '15:00', 'endtime': '16:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},

        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Thursday", 'starttime': '09:00', 'endtime': '10:30', 'leacture': 'Maths', 'lectProf': 'Dr. Smith'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Thursday", 'starttime': '11:00', 'endtime': '12:30', 'leacture': 'Physics', 'lectProf': 'Prof. Johnson'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Thursday", 'starttime': '13:00', 'endtime': '14:00', 'leacture': 'Science', 'lectProf': 'Prof. Johnny'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Thursday", 'starttime': '14:00', 'endtime': '15:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Thursday", 'starttime': '15:00', 'endtime': '16:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},

        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Friday", 'starttime': '09:00', 'endtime': '10:30', 'leacture': 'Maths', 'lectProf': 'Dr. Smith'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Friday", 'starttime': '11:00', 'endtime': '12:30', 'leacture': 'Physics', 'lectProf': 'Prof. Johnson'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Friday", 'starttime': '13:00', 'endtime': '14:00', 'leacture': 'Science', 'lectProf': 'Prof. Johnny'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Friday", 'starttime': '14:00', 'endtime': '15:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},
        {'branch': 'comps', 'year': 2024, 'div': 'a', 'day': "Friday", 'starttime': '15:00', 'endtime': '16:00', 'leacture': 'Physics', 'lectProf': 'Prof. Sahil'},
    ]


    sample_data = [
        {'imgpath': 'attendapp/setup/studentprofileimg/boy avatar.png', 'year': 2024, 'rollno': 101, 'name': 'John Doe', 'div': 'A', 'branch': 'comps', 'y1cgpa': 8.5, 'y1sgpa': 8.0, 'y2cgpa': 8.2, 'y2sgpa': 7.9, 'y3cgpa': 8.7, 'y3sgpa': 8.3, 'y4cgpa': 0.0, 'y4sgpa': 0.0, 'address': '123 Main Street', 'phoneno': '123-456-7890', 'parentphoneno': '987-654-3210', 'teachername': 'Sahil'},
        {'imgpath': 'attendapp/setup/studentprofileimg/boy avatar.png', 'year': 2024, 'rollno': 102, 'name': 'Alice Smith', 'div': 'B', 'branch': 'extc', 'y1cgpa': 8.8, 'y1sgpa': 8.2, 'y2cgpa': 8.6, 'y2sgpa': 8.1, 'y3cgpa': 8.9, 'y3sgpa': 8.4, 'y4cgpa': 0.0, 'y4sgpa': 0.0, 'address': '456 Oak Avenue', 'phoneno': '234-567-8901', 'parentphoneno': '876-543-2109', 'teachername': 'Sahil'},
        {'imgpath': 'attendapp/setup/studentprofileimg/boy avatar.png', 'year': 2024, 'rollno': 103, 'name': 'Michael Johnson', 'div': 'A', 'branch': 'aids', 'y1cgpa': 7.9, 'y1sgpa': 7.5, 'y2cgpa': 7.7, 'y2sgpa': 7.3, 'y3cgpa': 7.8, 'y3sgpa': 7.6, 'y4cgpa': 0.0, 'y4sgpa': 0.0, 'address': '789 Elm Street', 'phoneno': '345-678-9012', 'parentphoneno': '765-432-1098', 'teachername': 'John'},
        {'imgpath': 'attendapp/setup/studentprofileimg/boy avatar.png', 'year': 2024, 'rollno': 104, 'name': 'Emily Brown', 'div': 'B', 'branch': 'comps', 'y1cgpa': 8.3, 'y1sgpa': 7.8, 'y2cgpa': 8.0, 'y2sgpa': 7.6, 'y3cgpa': 8.5, 'y3sgpa': 8.1, 'y4cgpa': 0.0, 'y4sgpa': 0.0, 'address': '987 Pine Street', 'phoneno': '456-789-0123', 'parentphoneno': '654-321-0987', 'teachername': 'Sahil'},
        {'imgpath': 'attendapp/setup/studentprofileimg/boy avatar.png', 'year': 2024, 'rollno': 105, 'name': 'James Wilson', 'div': 'A', 'branch': 'comps', 'y1cgpa': 8.0, 'y1sgpa': 7.6, 'y2cgpa': 7.8, 'y2sgpa': 7.4, 'y3cgpa': 8.2, 'y3sgpa': 7.9, 'y4cgpa': 0.0, 'y4sgpa': 0.0, 'address': '246 Maple Street', 'phoneno': '567-890-1234', 'parentphoneno': '543-210-9876', 'teachername': 'Sahil'},
    ]

    # Save timetable entries to the database
    # for entry in timetable_entries:
    #     timetable_obj = TimeTable(**entry)
    #     timetable_obj.save()

    # for data in sample_data:
    #     student_profile = Studentprofile(**data)
    #     student_profile.save()

    # Get the current time
    # current_time = timezone.now().time()
    # current_day = datetime.datetime.now().strftime("%A")

    # # Query to check if the current time falls within the range in the database
    # lecture = TimeTable.objects.filter(
    #     day=current_day,
    #     starttime__lte=current_time,
    #     endtime__gte=current_time
    # ).first()

    # print("lecture ", lecture)
    return redirect('dashboard')

#         status = request.GET.get('status')

def viewbranch(request):
    # Check if the 'view' parameter exists in the request's GET parameters
    if 'view' in request.GET:
        # Get the value of the 'view' parameter
        view_param = request.GET['view']
        print("view_param : ", view_param)
        
        # Fetch all student profiles if 'view' parameter is not specified or its value is not 'extc'
        all_students = Studentprofile.objects.filter(branch=view_param, year=2024)
        params = {
            'all_students': all_students,
            'capbranch': view_param.capitalize(),
            'rawbranch': view_param,
        }
        return render(request, 'attendapp/viewbranch.html', params)
    
    # If 'view' parameter is not provided or its value is 'extc', redirect to dashboard
    return redirect('dashboard')


def todayattendence(request):
    # Get today's date
    # today_date = datetime.date.today()

    # Get the current time
    # current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.now().strftime("%A")


    # Filter attendance records for today
    attendance_records = Studattendence.objects.filter(day=current_day)
    print("current_day ", current_day)
    print("attendance_records ", attendance_records)

    params = {
        'attendance_records': attendance_records,
        'current_day': current_day,
        # 'rawbranch': view_param,
    }
    return render(request, 'attendapp/todayattendence.html', params)




# http://127.0.0.1:8000/viewstud/?rollno=105

def viewstud(request):
    # Check if the 'view' parameter exists in the request's GET parameters
    if 'rollno' in request.GET:
        # Get the value of the 'view' parameter
        view_param = request.GET['rollno']
        print("view_param : ", view_param)


        # Filter lectures for roll number 105 on the current day
        Studattendencedata = Studattendence.objects.filter(rollno=view_param)
        Studentprofiledata = Studentprofile.objects.filter(rollno=view_param).first()



        
        # Fetch all student profiles if 'view' parameter is not specified or its value is not 'extc'
        all_students = Studentprofile.objects.filter(rollno=view_param, year=2024).first()
        
        timetableMon = TimeTable.objects.filter(year='2024', branch=Studentprofiledata.branch, day='Monday')
        timetableTue = TimeTable.objects.filter(year='2024', branch=Studentprofiledata.branch, day='Tuesday')
        timetableWed = TimeTable.objects.filter(year='2024', branch=Studentprofiledata.branch, day='Wednesday')
        timetableThu = TimeTable.objects.filter(year='2024', branch=Studentprofiledata.branch, day='Thursday')
        timetableFri = TimeTable.objects.filter(year='2024', branch=Studentprofiledata.branch, day='Friday')





        params = {
            'studentsdetails': all_students,
            'capbranch': view_param.capitalize(),
            'rawbranch': view_param,

            'Studattendencedata': Studattendencedata,
            # 'current_day': current_day,

            'timetableMon': timetableMon,
            'timetableTue': timetableTue,
            'timetableWed': timetableWed,
            'timetableThu': timetableThu,
            'timetableFri': timetableFri,
        }
        return render(request, 'attendapp/viewstud.html', params)
    
    # If 'view' parameter is not provided or its value is 'extc', redirect to dashboard
    return redirect('dashboard')


# http://127.0.0.1:8000/markattendapi/?rollno=105

def markattendapi(request):
    if 'rollno' in request.GET:
        rollno = request.GET['rollno']
        
        # Check if student exists with the given rollno
        try:
            student = Studentprofile.objects.get(rollno=rollno)
            print("student: ", student)
        except Studentprofile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Student not found'}, status=404)
        
        # Check attendance status
        # current_time = datetime.datetime.now().time()
        # current_day = datetime.datetime.now().strftime("%A")

        current_time = timezone.now().time()
        current_day = datetime.datetime.now().strftime("%A")

        # Query to check if the current time falls within the range in the database
        lecture = TimeTable.objects.filter(
            day=current_day,
            starttime__lte=current_time,
            endtime__gte=current_time
        ).first()

        print("current_time: ", current_time, "current_day: ", current_day)
        print("lecture :", lecture)

        # lecture = TimeTable.objects.filter(day=current_day, starttime__lte=current_time, endtime__gte=current_time).first()
        
        if not lecture:
            return JsonResponse({'status': 'error', 'message': 'No lecture currently'}, status=400)
        
        # Check if attendance is already marked
        # existing_attendance = Studattendence.objects.filter(rollno=rollno, leacture=lecture.leacture, lectProf=lecture.lectProf, timestamp__date=datetime.date.today()).exists()
        # if existing_attendance:
        #     return JsonResponse({'status': 'error', 'message': 'Attendance already marked'}, status=400)
        
        # Mark attendance
        # Mark attendance
        attendance_record = Studattendence.objects.create(day=current_day, starttime=current_time, year='2024', rollno=rollno, leacture=lecture.leacture, lectProf=lecture.lectProf, timestamp=datetime.datetime.now())
        
        # Construct the JSON response with only necessary fields
        response_data = {
            'status': 'success',
            'message': 'Attendance marked successfully',
            'attendance_record': {
                'rollno': attendance_record.rollno,
                'leacture': attendance_record.leacture,
                'lectProf': attendance_record.lectProf,
                'timestamp': attendance_record.timestamp.isoformat(),  # Convert datetime to string
            }
        }
        
        return JsonResponse(response_data)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
    


def dashboard(request):
    # create_dummy_leave_dataset()
    teacher = User.objects.get(username=request.user.username)

    # Get all student profiles associated with the teacher's name
    student_profiles = Studentprofile.objects.filter(teachername=teacher.username)

    # Create lists for unique branch, div, and year
    unique_branches = student_profiles.values_list('branch', flat=True).distinct()
    unique_divs     = student_profiles.values_list('div', flat=True).distinct()
    unique_years    = student_profiles.values_list('year', flat=True).distinct()

    # Print all unique branches, divs, and years
    print("Unique Branches:")
    for branch in unique_branches:
        print(branch)

    print("\nUnique Divisions:")
    for div in unique_divs:
        print(div)

    print("\nUnique Years:")
    for year in unique_years:
        print(year)    
    

    params = {
        "unique_branches" : unique_branches,
        "unique_divs" : unique_divs,
        "unique_years" : unique_years,
        # "exp_type_counts" : attend,
    }

    return render(request, 'attendapp/dashboard.html', params)


# def addnewuser(request):
    # return render(request, 'attendapp/addnewuser.html')

# def addnewuser(request):
#     if request.method == 'POST':
#         # Get data from the form
#         fullname = request.POST.get('fullname')
#         email = request.POST.get('email')
#         department = request.POST.get('department')
#         jobtitle = request.POST.get('jobtitle')
#         user_name = request.POST.get('user_name')
#         password = request.POST.get('password')
#         phoneno = request.POST.get('phoneno')
#         address = request.POST.get('address')
#         gender = request.POST.get('gender')
#         dateofbirth = request.POST.get('dateofbirth')
#         MaritalStatus = request.POST.get('MaritalStatus')
#         EmployeePhotoPath = request.POST.get('EmployeePhotoPath')
#         role = request.POST.get('role')
#         department = request.POST.get('department')
#         jobtitle = request.POST.get('jobtitle')
#         manager = request.POST.get('manager')
#         dateofjoin = request.POST.get('dateofjoin')
#         status = request.POST.get('status')
#         EmpStatus = request.POST.get('EmpStatus')
#         EmpType = request.POST.get('EmpType')
#         WorkLoc = request.POST.get('WorkLoc')

#         # Create an instance of Employaccdata model and assign values
#         employ_data = Employaccdata(
#             fullname=fullname,
#             email=email,
#             department=department,
#             jobtitle=jobtitle,
#             user_name=user_name,
#             password=password,
#             phoneno=phoneno,
#             address=address,
#             gender=gender,
#             dateofbirth=dateofbirth,
#             MaritalStatus=MaritalStatus,
#             EmployeePhotoPath=EmployeePhotoPath,
#             role=role,
#             manager=manager,
#             dateofjoin=dateofjoin,
#             status=status,
#             EmpStatus=EmpStatus,
#             EmpType=EmpType,
#             WorkLoc=WorkLoc
#         )

#         # Save the instance to the database
#         employ_data.save()

#         return redirect(attendencemanage)
#     else:
#         # return HttpResponse("Invalid request method. Only POST requests are allowed.")
#         return render(request, 'attendapp/addnewuser.html')














# def updateleavestat(request):
#     if request.method == 'GET':
#         # Get the leave_id and status from the request
#         leave_id = request.GET.get('leave_id')
#         status = request.GET.get('status')

#         # Get the Leave instance using leave_id
#         leave_instance = get_object_or_404(Leave, leave_id=leave_id)

#         # Update the status of the Leave instance
#         leave_instance.status = status
#         leave_instance.save()

#         # return JsonResponse({'message': 'Leave status updated successfully'}, status=200)
#         redirect_url = '/leavemanage/?view=all'
#         return redirect(redirect_url)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)





# def calculate_time_difference(checkin, checkout):
#     # Parse the checkin and checkout times into datetime objects
#     checkin_time = datetime.strptime(checkin, "%H:%M")
#     checkout_time = datetime.strptime(checkout, "%H:%M")

#     # Calculate the time difference
#     time_difference = checkout_time - checkin_time

#     # Return the time difference as a timedelta object
#     return time_difference


# def attendencemanage(request):
#     attend = Employaccdata.objects.all()

#     drifftlist = [] 
#     # calculate_time_difference(checkin, checkout)
#     # Iterate over each attendance record
#     for attendance in attend:
#         # Calculate time difference for this attendance record
#         time_diff = calculate_time_difference(attendance.Checkin, attendance.Checkout)
#         drifftlist.append(time_diff)
#         # Print the result
#         # print(f"User: {attendance.user_name}, Time Difference: {time_diff}")


#     params = {
#         "attend" : attend,
#         "drifftlist" : drifftlist,
#         # "exp_type_counts" : attend,
#     }
#     return render(request, 'attendapp/attendence.html', params)



# def filter_leave_data(user_name):
#     # Filter Leave instances based on the provided user_name
#     leave_data = Leave.objects.filter(user_name=user_name)

#     # Initialize leave count dictionary
#     leave_count = {leave_type: 0 for leave_type in ['Sick', 'Privilege', 'Casual', 'Maternity/Paternity']}

#     # Calculate leave count for each type
#     for leave in leave_data:
#         if leave.leave_type in leave_count:
#             leave_count[leave.leave_type] += 1

#     # Edit the list according to leave count
#     updated_list = []
#     for leave_type, count in leave_count.items():
#         updated_list.append(count)

#     return updated_list

# def employprofile(request):
#     view_type = request.GET.get('profileid')
#     employdata = Employaccdata.objects.filter(eacc_id=view_type)

#     spiderchartdata = [0, 0, 0, 0, 0]
#     for employaccdata in employdata:
#         print("eacc_id:", employaccdata.eacc_id)
#         print("Productivityvalue:", employaccdata.Productivityvalue)
#         print("Satisfactionvalue:", employaccdata.Satisfactionvalue)
#         print("FeedbackScorevalue:", employaccdata.FeedbackScorevalue)
#         print("Skillsvalue:", employaccdata.Skillsvalue)
#         print("Communicationvalue:", employaccdata.Communicationvalue)

#         leavedata = filter_leave_data(employaccdata.user_name)
#         print("leavedata : ", leavedata)
#         print("employaccdata.user_name : ", employaccdata.user_name)

#         # [{'leave_type': 'Sick', 'count': 1}, {'leave_type': 'Privilege', 'count': 0}, {'leave_type': 'Casual', 'count': 0}, {'leave_type': 'Maternity/Paternity', 'count': 0}]   

#         # Iterate over the list to find the count for leave_type = 'Sick'
#         # for item in leavedata:
#         #     if item['leave_type'] == 'Sick':
#         #         spiderchartdata[0] = item['count']
#         #     if item['leave_type'] == 'Privilege':
#         #         spiderchartdata[1] = item['count']
#         #     if item['leave_type'] == 'Casual':
#         #         spiderchartdata[2] = item['count']
#         #     if item['leave_type'] == 'Maternity/Paternity':
#         #         spiderchartdata[3] = item['count']

#         spiderchartdata[0] = leavedata[0]
#         spiderchartdata[1] = leavedata[1]
#         spiderchartdata[2] = leavedata[2]
#         spiderchartdata[3] = leavedata[3]


#     params = {
#         "employdata" : employdata,
#         "spiderchartdata" : spiderchartdata,
#     }
#     return render(request, 'attendapp/employprofile.html', params)

# # http://127.0.0.1:8000/employprofile/?profileid=1


# def reimbusmentmanage(request):
#     view_type = request.GET.get('view')

#     if view_type == 'all':
#         # Get all reimbursements
#         reimbus = Reimbusement.objects.all()
#     elif view_type == 'Pending':
#         # Get reimbursements with status 'Pending'
#         reimbus = Reimbusement.objects.filter(status=view_type)
#     elif view_type in ['Travel', 'Accomodation', 'BusinessMeals', 'Miscellaneous']:
#         # Get reimbursements based on expense_type
#         reimbus = Reimbusement.objects.filter(expense_type=view_type)
#     else:
#         # Handle invalid or missing view parameter
#         return JsonResponse({'error': 'Invalid or missing view parameter'}, status=400)


#     # Serialize the reimbus data
#     serialized_data = [{
#         'reimbus_id': leave.reimbus_id,
#         'department': leave.department,
#         'user_name': leave.user_name,
#         'date': leave.date.strftime('%Y-%m-%d'),
#         'expense_type': leave.expense_type,
#         'amount': leave.amount,
#         'shortdesc': leave.shortdesc,
#         'status': leave.status,
#         'paymenttype': leave.paymenttype,
#     } for leave in reimbus]

#     serialized_data_inverted = serialized_data[::-1]


#     # create_dummy_leave_dataset()
#     # delete_all_reimbursements()
#     expense_typelist = ['Travel', 'Accomodation', 'BusinessMeals', 'Miscellaneous']
#     exp_type_counts = [0, 0, 0, 0]
#     # Count the number of records where expense_type matches expense_type_to_count
#     exp_type_counts[0] = Reimbusement.objects.filter(expense_type=expense_typelist[0]).count()
#     exp_type_counts[1] = Reimbusement.objects.filter(expense_type=expense_typelist[1]).count()
#     exp_type_counts[2] = Reimbusement.objects.filter(expense_type=expense_typelist[2]).count()
#     exp_type_counts[3] = Reimbusement.objects.filter(expense_type=expense_typelist[3]).count()

#     # Retrieve data from the Reimbursement model
#     # reimbursements = Reimbusement.objects.all()

#     # Invert the list
#     # inverted_reimbursements = reversed(reimbursements)

#     params = {
#         "reimbursements" : serialized_data_inverted,
#         "exp_type_counts" : exp_type_counts,
#     }

#     return render(request, 'attendapp/reimbusment.html', params)

# def updatereimbusment(request):
#     if request.method == 'GET':
#         # Get the leave_id and status from the request
#         reimbus_id = request.GET.get('reimbus_id')
#         status = request.GET.get('status')

#         # Get the Leave instance using leave_id
#         leave_instance = get_object_or_404(Reimbusement, reimbus_id=reimbus_id)

#         # Update the status of the Leave instance
#         leave_instance.status = status
#         leave_instance.save()

#         # return JsonResponse({'message': 'Leave status updated successfully'}, status=200)
#         redirect_url = '/reimbusmentmanage/?view=all'
#         return redirect(redirect_url)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)


# '''

# http://127.0.0.1:8000/reimbusmentmanage/?view=all

# http://127.0.0.1:8000/updatereimbusment/?reimbus_id=28&status=Approved
# '''


# # http://127.0.0.1:8000/update_employee/?eacc_id=1&status=Working&Checkin=09:00&Checkout=17:00


# # http://127.0.0.1:8000/create_reimbursement/?department=Finance&user_name=shaun&date=2024-04-07&expense_type=Travel&amount=200&shortdesc=Travel%20expense&pdfpath=/path/to/pdf&status=Pending&paymenttype=check&days=2

# def create_reimbursement_record(request):
#     if request.method == 'GET':
#         # Retrieve data from query parameters
#         department = request.GET.get('department', '')
#         user_name = request.GET.get('user_name', '')
#         date = request.GET.get('date', '')
#         expense_type = request.GET.get('expense_type', '')
#         amount = request.GET.get('amount', '')
#         shortdesc = request.GET.get('shortdesc', '')
#         pdfpath = request.GET.get('pdfpath', '')
#         status = request.GET.get('status', '')
#         paymenttype = request.GET.get('paymenttype', '')
#         days = request.GET.get('days', '')

#         # Create Reimbursement instance
#         reimbursement = Reimbusement.objects.create(
#             department=department,
#             user_name=user_name,
#             date=date,
#             expense_type=expense_type,
#             amount=amount,
#             shortdesc=shortdesc,
#             pdfpath=pdfpath,
#             status=status,
#             paymenttype=paymenttype,
#             days=days
#         )

#         # Return JSON response indicating success
#         return JsonResponse({'message': 'Reimbursement record created successfully'}, status=201)

#     # If the request method is not GET, return an error response
#     return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)





# # http://127.0.0.1:8000/update_employee/?eacc_id=1&status=Working&Checkin=09:00&Checkout=17:00


# def update_employee(request):
#     if request.method == 'GET':
#         # Get the leave_id and status from the request
#         eacc_id = request.GET.get('eacc_id')

#         employee = get_object_or_404(Employaccdata, pk=eacc_id)
#         checkin = request.GET.get('Checkin')
#         Checkout = request.GET.get('Checkout')
#         print("checkin: ", checkin, "Checkout : ", Checkout)
#         # calculate_time_difference(checkin, Checkout)

#         employee.status = request.GET.get('status')
#         employee.Checkin = request.GET.get('Checkin')
#         employee.Checkout = request.GET.get('Checkout')
#         employee.save()


#         # return JsonResponse({'message': 'Leave status updated successfully'}, status=200)
#         # redirect_url = '/leavemanage/?view=all'

#         # return redirect(redirect_url)
#         return JsonResponse({'success': 'success method'}, status=405)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)


# # # update_employee/1/
# # def update_employee(request, eacc_id):
# #     # Retrieve the employee object
# #     employee = get_object_or_404(Employaccdata, pk=eacc_id)

# #     if request.method == 'GET':
# #         employee.status = request.POST.get('status')
# #         employee.Checkin = request.POST.get('Checkin')
# #         employee.Checkout = request.POST.get('Checkout')

# #         # Save the changes
# #         employee.save()

# #         # Redirect to a success URL or render a success template
# #         # return redirect('success-url')  # Replace 'success-url' with the name of your success URL pattern
# #         return HttpResponse("saved successfully.")


# #     # Render a form with the current data for the employee
# #     return HttpResponse("Simple request.")
# #     # return render(request, 'update_employee.html', {'employee': employee})



# def hrbot(request):
#     user_name = request.user.username

#     chat_data = Chatdata.objects.filter(user_name=user_name)

#     params = {
#         "chat_data" : chat_data,
#     }

#     return render(request, 'attendapp/hrbotpage.html', params)

# def chatbot(text_to_encode):
#     # text_to_encode = 'what is ai in real world' # @param {isTemplate: true}
#     encoded_text_b64 = base64.b64encode(text_to_encode.encode()).decode()
#     print("Received")
#     # user_input_b64 = 'd2hhdCBpcyBhaSBpbiByZWFsIHdvcmxk'  # Example base64-encoded string with padding
#     user_input_b64 = encoded_text_b64  # Example base64-encoded string with padding

#     # Add padding characters if needed
#     while len(user_input_b64) % 4 != 0:
#         user_input_b64 += '='
#     print("Generating")
#     contents = json.loads(base64.b64decode(contents_b64))
#     generation_config = json.loads(base64.b64decode(generation_config_b64))
#     safety_settings = json.loads(base64.b64decode(safety_settings_b64))
#     user_input = base64.b64decode(user_input_b64).decode()
#     stream = False
#     gemini = genai.GenerativeModel(model_name=model)
#     print("Done")
#     chat = gemini.start_chat(history=contents)

#     response = chat.send_message(
#         user_input,
#         stream=stream)
#     reply=response.text.replace("*","")
#     reply=reply.replace("\n","")
#     return reply

# def chatinput(request):
#     help_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five':5,
#     'six': 6,
#     'seven': 7,
#     'eight': 8,
#     'nine': 9,
#     'zero': 0,
#     'ten':10
#     }

#     reply=""
#     if request.method == 'POST':
#         query = request.POST.get('name')
#         user_name = request.POST.get('user_name')
#         servicetype  = Employaccdata.objects.filter(user_name=user_name)

#         if "shaun" in query:
#             user_name = "shaun"
#         elif "ryan" in query:
#             user_name = "ryan"
#         elif "atharvapawar" in query:
#             user_name = "atharvapawar"

#         if "reimbursement" in query:
#             # servicetype = "shaun"Reimbusement.objects.all()
#             q=query.split(" ")
#             if "last" in q:
#                 print(q.index('last')+1)
#                 recent=help_dict[q[q.index('last')+1]] #last ten
#                 reply="Getting it for you"
#                 f"select * from Reimbusement Limit {recent}"
#                 last_10_records = Reimbusement.objects.filter(user_name='ryan').order_by('-reimbus_id')[:recent]

#                 print("last_10_records" , last_10_records)

#                 params = {
#                     "last_10_records" : last_10_records,
#                 }

#                 return render(request, 'attendapp/hrbotpage.html', params)

#         elif "leave" in query:
#             leave_objects =  Leave.objects.values_list('leave_id', 'reason')
#             leavereasonlist=list(leave_objects)
#             print(leavereasonlist)
#             a=str(leavereasonlist).replace('(',"")
#             a=a.replace(')','')
#             leavetemplate=f"I am giving you a list of id and their respective reasons for leave , you need to arrange them in the decreasing order of priority This is the list {a}"
#             reply=chatbot(leavetemplate)
#             print(reply)
#         # result_text = ""
#         # for obj in leave_objects:
#         #     result_text += f"Reimbursement ID: {obj.reimbus_id}\n"
#         #     result_text += f"Department: {obj.department}\n"
#         #     result_text += f"User Name: {obj.user_name}\n"
#         #     result_text += f"Date: {obj.date}\n"
#         #     result_text += f"Expense Type: {obj.expense_type}\n"
#         #     result_text += f"Amount: {obj.amount}\n"
#         #     result_text += f"Short Description: {obj.shortdesc}\n"
#         #     servicetype += "\n"


#         # elif "leave" in query:
#         #     # servicetype = "ryan"
#         #     leave_objects = Leave.objects.filter(user_name=user_name)
#         #     result_text = ""
#         #     for obj in leave_objects:
#         #         result_text += f"Reimbursement ID: {obj.leave_id}\n"
#         #         result_text += f"Department: {obj.department}\n"
#         #         result_text += f"User Name: {obj.user_name}\n"
#         #         result_text += f"Date: {obj.date}\n"
#         #         result_text += f"leave_type: {obj.leave_type}\n"
#         #         result_text += f"Amount: {obj.reason}\n"
#         #         result_text += f"Short Description: {obj.status}\n"
#         #         servicetype += "\n"

#         elif "employee" or "employees" or "work" in query:
#             employee_objects =  Employaccdata.objects.values_list('eacc_id', 'department')
#             # names = re.findall(r'\b[A-Z][a-z]*\b', query)[0]
#             names=""
#             for i in query:
#                 if i in ['Web Development','Data Analytics','IoT','Computer']:
#                     names=i
#                     break
#             empdeptlist=list(employee_objects)
#             print(names)
#             print(empdeptlist)
#             print("This is the ans")
#             b=str(empdeptlist).replace('(',"")
#             b=b.replace(')','')
#             emptemplate=f"I am giving you a list of all the employee details you need to extract the id of all the employees whoose department is {names} The data set is {b}"
#             reply=chatbot(emptemplate)
#             # print(reply)

#         #     # servicetype = "atharvapawar"
#         #     leave_objects = Employaccdata.objects.filter(user_name=user_name)
#         #     result_text = ""
#         #     for obj in leave_objects:
#         #         result_text += f"Reimbursement ID: {obj.eacc_id}\n"
#         #         result_text += f"Department: {obj.department}\n"
#         #         result_text += f"User Name: {obj.user_name}\n"
#         #         result_text += f"jobtitle: {obj.jobtitle}\n"
#         #         result_text += f"manager: {obj.manager}\n"
#         #         result_text += f"EmpStatus: {obj.EmpStatus}\n"
#         #         result_text += f"EmpType: {obj.EmpType}\n"
#         #         result_text += f"WorkLoc: {obj.WorkLoc}\n"
#         #         result_text += f"role: {obj.role}\n"
#         #         servicetype += "\n"


#         print("servicetype" , servicetype)
#         print("user_name" , user_name)
#         template = "_"
#         template = template + f"{user_name} This is data from the database use this data and answer the folling query "
#         template = template + f"{query}"
#         print("template : ", template)

#         # reply = chatbot(template)

#         # Create a new record in the Chatdata model
#         new_chat_record = Chatdata.objects.create(
#             user_name=user_name,
#             query=query,
#             shortdesc=reply
#         )

#         # Optionally, you can save the new record explicitly
#         # new_chat_record.save()

#         return redirect(hrbot)
#     else:
#         return HttpResponse('Invalid request method. Only POST requests are allowed for this endpoint.')






# def hrnotification(request):

#     return render(request, 'attendapp/notification.html')

# def hrmail(request):
#     return render(request, 'attendapp/notification.html')




# # http://localhost:8000/leavecreate/?department=HR&user_name=John&leave_type=Vacation&days=2&reason=Family%20time&status=Pending

# def leave_create(request):
#     if request.method == 'GET':
#         # Retrieve data from query parameters
#         department = request.GET.get('department', 'Sample Department')
#         user_name = request.GET.get('user_name', 'Sample User')
#         date = "2024-04-07"
#         # YYYY-MM-DD
#         leave_type = request.GET.get('leave_type', 'Sample Leave Type')
#         days = request.GET.get('days', 1)
#         reason = request.GET.get('reason', 'Sample Reason')
#         status = request.GET.get('status', 'Pending')

#         # Convert days to integer
#         try:
#             days = int(days)
#         except ValueError:
#             days = 1

#         # Create Leave instance and save it to the database
#         leave = Leave.objects.create(
#             department=department,
#             user_name=user_name,
#             date=date,
#             leave_type=leave_type,
#             days=days,
#             reason=reason,
#             status=status
#         )
#         leave.save()

#         return HttpResponse("Leave instance created and saved successfully.")
#     else:
#         return HttpResponse("Invalid request method.")


# def leavemanage(request):
#     view_type = request.GET.get('view')

#     if view_type == 'all':
#         # Get all reimbursements
#         leaves = Leave.objects.all()
#     elif view_type == 'Pending':
#         # Get reimbursements with status 'Pending'
#         leaves = Leave.objects.filter(status=view_type)
#     elif view_type in ['Sick', 'Privilege', 'Casual', 'Maternity/Paternity']:
#         # Get reimbursements based on expense_type
#         leaves = Leave.objects.filter(leave_type=view_type)
#     else:
#         # Handle invalid or missing view parameter
#         return JsonResponse({'error': 'Invalid or missing view parameter'}, status=400)




#     # Serialize the leaves data
#     serialized_data = [{
#         'leave_id': leave.leave_id,
#         'department': leave.department,
#         'user_name': leave.user_name,
#         'date': leave.date.strftime('%Y-%m-%d'),
#         'leave_type': leave.leave_type,
#         'days': leave.days,
#         'reason': leave.reason,
#         'llmsuggest': leave.llmsuggest,
#         'status': leave.status
#     } for leave in leaves]

#     serialized_data_inverted = serialized_data[::-1]

#     leave_types = ['Sick', 'Privilege', 'Casual', 'Maternity/Paternity']

#     leave_type_counts = [0, 0, 0, 0]
#     # Count the number of records where expense_type matches expense_type_to_count
#     leave_type_counts[0] = Leave.objects.filter(leave_type=leave_types[0]).count()
#     leave_type_counts[1] = Leave.objects.filter(leave_type=leave_types[1]).count()
#     leave_type_counts[2] = Leave.objects.filter(leave_type=leave_types[2]).count()
#     leave_type_counts[3] = Leave.objects.filter(leave_type=leave_types[3]).count()


#     params = {
#         "leavedata" : serialized_data_inverted,
#         "leave_type_counts" : leave_type_counts,

#     }
#     # return JsonResponse(serialized_data, safe=False)
#     return render(request, 'attendapp/leavemanage.html', params)


# def updateleavestat(request):
#     if request.method == 'GET':
#         # Get the leave_id and status from the request
#         leave_id = request.GET.get('leave_id')
#         status = request.GET.get('status')

#         # Get the Leave instance using leave_id
#         leave_instance = get_object_or_404(Leave, leave_id=leave_id)

#         # Update the status of the Leave instance
#         leave_instance.status = status
#         leave_instance.save()

#         # return JsonResponse({'message': 'Leave status updated successfully'}, status=200)
#         redirect_url = '/leavemanage/?view=all'
#         return redirect(redirect_url)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)

'''

http://127.0.0.1:8000/leavemanage/?view=Privilege

http://127.0.0.1:8000/updateleavestat/?leave_id=28&status=Approved
'''
# def delete_all_reimbursements():
#     try:
#         Reimbusement.objects.all().delete()
#         print("All data deleted successfully")
#     except IntegrityError as e:
#         print(f"Error deleting data: {e}")

# def create_dummy_leave_dataset():

# #     sick_leave_reasons = [
# #     "Fever and flu symptoms persisting for several days.",
# #     "Severe headache and body ache causing discomfort.",
# #     "Doctor advised bed rest due to respiratory infection.",
# #     "Recovering from a minor surgical procedure at the hospital.",
# #     "Nausea and vomiting due to food poisoning.",
# #     "Migraine attacks affecting productivity and concentration.",
# #     "Experiencing severe back pain hindering mobility.",
# #     "Allergic reaction causing skin rash and itching.",
# #     "Chronic illness flare-up requiring immediate medical attention.",
# #     "Sudden onset of stomach cramps and diarrhea."
# # ]

# #     privilege_leave_reasons = [
# #         "Celebrating a special occasion with family and friends.",
# #         "Taking a short vacation to rejuvenate and relax.",
# #         "Attending a family wedding ceremony out of town.",
# #         "Participating in a cultural festival in the hometown.",
# #         "Visiting relatives and spending quality time with them.",
# #         "Renovating home and overseeing construction work.",
# #         "Completing pending personal errands and tasks.",
# #         "Taking a break to focus on personal hobbies and interests.",
# #         "Attending a career development workshop or seminar.",
# #         "Volunteering for a social cause and community service."
# #     ]

# #     casual_leave_reasons = [
# #         "Attending a medical appointment or health checkup.",
# #         "Sudden family emergency requiring immediate attention.",
# #         "Attending a parent-teacher meeting at child's school.",
# #         "Rescheduling personal commitments and appointments.",
# #         "Participating in a sports or recreational activity.",
# #         "Attending a friend's birthday celebration or party.",
# #         "Going for a shopping trip to buy essential items.",
# #         "Taking a day off to relax and unwind at home.",
# #         "Dealing with unexpected household repairs or maintenance.",
# #         "Traveling for a short trip or weekend getaway."
# #     ]

# #     maternity_paternity_leave_reasons = [
# #         "Welcoming a new addition to the family with newborn care.",
# #         "Supporting spouse during childbirth and postpartum recovery.",
# #         "Bonding with the newborn and adjusting to new family dynamics.",
# #         "Attending prenatal checkups and childbirth classes.",
# #         "Taking time off to be with the newborn and help with childcare.",
# #         "Adopting a child and spending quality time with the new family member.",
# #         "Supporting partner during adoption process and transition.",
# #         "Arranging for childcare arrangements and family support.",
# #         "Managing household responsibilities during parental leave.",
# #         "Preparing for parenthood and adjusting to new routines."
# #     ]

#     Travel = [
#         'Flight tickets',
#         'Taxi fare',
#         'Car rental',
#         'Parking fees',
#         'Train tickets',
#         'Gasoline',
#         'Toll fees',
#         'Visa fees',
#         'Baggage fees',
#         'Public transportation fares',
#     ]
#     Accomodation = [
#         'Hotel stay',
#         'Resort booking',
#         'Airbnb rental',
#         'Hostel accommodation',
#         'Cabin rental',
#         'Motel stay',
#         'Bed and breakfast',
#         'Luxury hotel suite',
#         'Dormitory booking',
#         'Vacation rental',
#     ]
#     BusinessMeals = [
#         'Dinner meeting',
#         'Lunch with partner',
#         'Coffee meeting',
#         'Breakfast during event',
#         'Team lunch',
#         'Client entertainment',
#         'Happy hour drinks',
#         'Business dinner',
#         'Conference lunch',
#         'Breakfast meeting',
#     ]
#     Miscellaneous = [
#         'Office supplies purchase',
#         'Printing and photocopying charges',
#         'Software subscription renewal',
#         'Membership fee',
#         'Business card printing',
#         'Internet and phone bill',
#         'Conference registration fee',
#         'Transportation expenses',
#         'Gift for client or colleague',
#         'Charitable donation',
#     ]

# #     leave_types = ['Sick', 'Privilege', 'Casual', 'Maternity/Paternity']
#     expense_typelist = ['Travel', 'Accomodation', 'BusinessMeals', 'Miscellaneous']
#     departments = ['HR', 'Finance', 'IT', 'Operations']
#     statuses = ['Pending', 'Approved', 'Rejected']
#     paymenttype = ['check','deposit']

#     for _ in range(40):
#         # Choose random values for department, user_name, leave_type, reason, and status
#         department = choice(departments)
#         user_name = "Employee" + str(_)
#         date = timezone.now()
#         expense_type = choice(expense_typelist)
#         days = str(1)  # Assuming each leave is for one day, you can change this as needed
#         status = choice(statuses)
#         # Select a random reason based on the leave type
#         if expense_type == 'Travel':
#             shortdesc = choice(Travel)
#         elif expense_type == 'Accomodation':
#             shortdesc = choice(Accomodation)
#         elif expense_type == 'BusinessMeals':
#             shortdesc = choice(BusinessMeals)
#         elif expense_type == 'Miscellaneous':
#             shortdesc = choice(Miscellaneous)

#         # Create Leave instance and save it to the database
#         Reimbusementdata = Reimbusement.objects.create(
#             department=department,
#             user_name=user_name,
#             date=date,
#             expense_type=expense_type,
#             amount=random.randint(100, 20000),
#             days=days,
#             shortdesc=shortdesc,
#             pdfpath="static/attendapp/reimbuspdf",
#             status=status,
#             paymenttype=choice(paymenttype)
#         )
#         Reimbusementdata.save()

# Call the function to create the dataset
# create_dummy_leave_dataset()


'''
    department = models.CharField(max_length=100, default="")
    user_name = models.CharField(max_length=255, default="")
    date = models.DateField()
    expense_type = models.CharField(max_length=50, default="")
    amount = models.CharField(max_length=100, default="")
    days = models.CharField(max_length=50, default="")
    shortdesc = models.TextField()
    pdfpath = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, default="")
    paymenttype = models.CharField(max_length=50, default="") #check/deposit

'''


# def oneemploy(request):
#     if 'user_name' in request.GET:
#         user_name = request.GET['user_name']
#         employ_data = Employaccdata.objects.filter(user_name=user_name)
#         if employ_data.exists():
#             return HttpResponse(employ_data.values())
#         else:
#             return HttpResponse("No data found for user_name: {}".format(user_name))
#     else:
#         return HttpResponse("user_name parameter is missing.")

# def oneLeave(request):
#     if 'user_name' in request.GET:
#         user_name = request.GET['user_name']
#         leave_data = Leave.objects.filter(user_name=user_name)
#         if leave_data.exists():
#             return HttpResponse(leave_data.values())
#         else:
#             return HttpResponse("No data found for user_name: {}".format(user_name))
#     else:
#         return HttpResponse("user_name parameter is missing.")

# def oneReimbusement(request):
#     if 'user_name' in request.GET:
#         user_name = request.GET['user_name']
#         reimbusement_data = Reimbusement.objects.filter(user_name=user_name)
#         if reimbusement_data.exists():
#             return HttpResponse(reimbusement_data.values())
#         else:
#             return HttpResponse("No data found for user_name: {}".format(user_name))
#     else:
#         return HttpResponse("user_name parameter is missing.")



'''
http://127.0.0.1:8000/oneemploy/?user_name=shaun
http://127.0.0.1:8000/oneLeave/?user_name=shaun
http://127.0.0.1:8000/oneReimbusement/?user_name=shaun

'''














# Ref : Old Data

# @login_required
# def viewNodes(request):
#     try:

#         user_nodes = Nodedata.objects.filter(user_name=request.user.username)
#         user_clusterdata = Clusterdata.objects.filter(
#             user_name=request.user.username)
#         # print("user_nodes : ", user_nodes)
#         # print("username : ", request.user.username)

#         # Pass the list of nodes to the template
#         context = {
#             'user_nodes': user_nodes,
#             'user_clusterdata': user_clusterdata,
#         }
#         return render(request, 'agroapp/nodes.html', context)

#     except:
#         return render(request, 'agroapp/nodes.html')


# @login_required
# def addnode(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         node_name = request.POST.get('node_name')
#         Loc_lat = request.POST.get('lat')
#         Loc_long = request.POST.get('long')
#         api_key = generate_unique_api_key()

#         # Create a new node
#         Nodedata.objects.create(user_name=user_name,
#                                 node_name=node_name,
#                                 Loc_lat=Loc_lat,
#                                 Loc_long=Loc_long,
#                                 api_key=api_key)

#         # Redirect to a success page or another view
#         return redirect(
#             'viewNodes'
#         )  # Change 'node_list' to the actual URL name for the node list view

#     return render(request, 'agroapp/addnode.html')


# @login_required
# def addcluster(request):
#     if request.method == 'POST':
#         selected_nodes = request.POST.getlist('selected_nodes')
#         user_name = request.user.username
#         cluster_name = request.POST.get('cluster_name')

#         print("Selected Nodes:", selected_nodes, user_name, cluster_name)

#         # Create a new node
#         Clusterdata.objects.create(user_name=user_name,
#                                    cluster_name=cluster_name,
#                                    clust_data=selected_nodes)

#         # Redirect to a success page or another view
#         return redirect(
#             'viewNodes'
#         )  # Change 'node_list' to the actual URL name for the node list view

#     user_nodes = Nodedata.objects.filter(user_name=request.user.username)
#     context = {
#         'user_nodes': user_nodes,
#     }
#     return render(request, 'agroapp/addcluster.html', context)


# def get_the_map(lat, long, node_name):
#     # Specify the latitude and longitude
#     # lat, lon = 123.13, 123.34

#     # Create a Folium map centered at the specified location
#     my_map = folium.Map(location=[lat, long], zoom_start=16)

#     # Add a marker at the specified location
#     folium.Marker([lat, long], popup=node_name).add_to(my_map)
#     # folium.Marker([lat, long], popup=node_name, icon=folium.Icon(color='red')).add_to(my_map)

#     # Convert the map to HTML
#     map_html = my_map._repr_html_()
#     return map_html

#     # Pass the HTML content to the template
#     # return render(request, 'mymaps.html', {'map_html': map_html})


# def get_the_map_multipal_loc(locations):
#     # Create a Folium map centered at the first location
#     first_location = locations[0]

#     my_map = folium.Map(
#         location=[first_location['lat'], first_location['long']],
#         zoom_start=16)

#     # Add markers for each location
#     for location in locations:
#         folium.Marker([location['lat'], location['long']],
#                       popup=location['node_name']).add_to(my_map)

#     # Convert the map to HTML
#     map_html = my_map._repr_html_()
#     return map_html


# # @login_required
# def viewNodeData(request):
#     # Get parameters from the GET request

#     # username = request.GET.get('username', '')  # Hacker Trap
#     # username = request.user.username
#     nodename = request.GET.get('nodename', '')
#     # lat = request.GET.get('lat', '')
#     # long = request.GET.get('long', '')

#     if Nodedata.objects.filter(node_name=nodename).exists():
#         # Use the parameters as needed in your view logic
#         try:
#             # Example: Retrieve sensor data based on the node name

#             sensor_data = SensorData.objects.filter(
#                 nodename=nodename).order_by('-timestamp')
#             # sensor_data = SensorData.objects.filter(nodename=nodename)

#             # Retrieve the latest data for the specified nodename
#             latest_sensor_data = SensorData.objects.filter(
#                 nodename=nodename).order_by('-timestamp').first()

#             latest_5_sensor_data_list = SensorData.objects.filter(
#                 nodename=nodename).order_by('-timestamp')[:5]
#             latest_5_sensor_data_list = latest_5_sensor_data_list[::-1]

#             # if not latest_5_sensor_data_list:
#             # latest_5_sensor_data_list = latest_sensor_data
#             # latest_sensor_data = "null"

#         except:
#             sensor_data = "null"
#             latest_sensor_data = "null"
#             latest_5_sensor_data_list = "null"

#         user_node_data = Nodedata.objects.filter(node_name=nodename).first()

#         if user_node_data:
#             api_key = user_node_data.api_key
#             user_name = user_node_data.user_name
#             lat = user_node_data.Loc_lat
#             long = user_node_data.Loc_long
#         else:
#             api_key = 'Not available'
#             user_name = 'Not available'
#             lat = 'Not available'
#             long = 'Not available'

#         map_html = get_the_map(lat, long, nodename)

#         # Pass data to the template
#         context = {
#             'username': user_name,
#             'nodename': nodename,
#             'lat': lat,
#             'long': long,
#             'api_key': api_key,
#             'sensor_data': sensor_data,
#             'latest_data': latest_sensor_data,
#             'map_html': map_html,
#             'latest_5_sensor_data_list': latest_5_sensor_data_list,
#         }
#         return render(request, 'agroapp/nodedata.html', context)
#     else:
#         context = {"message": "wrong_route"}
#         return render(request, 'agroapp/nodedata.html', context)


# # @login_required
# def viewclusterData(request):

#     # username = request.GET.get('username', '')  # Hacker Trap
#     # username = request.user.username
#     clustername = request.GET.get('clustername', '')

#     if Clusterdata.objects.filter(cluster_name=clustername).exists():
#         try:

#             cluster_data = Clusterdata.objects.filter(cluster_name=clustername)
#             # Extract 'clust_data' from each object and store it in a list
#             list_of_clust_data = [entry.clust_data for entry in cluster_data]

#             all_node_names = ast.literal_eval(list_of_clust_data[0])
#             all_nodeData = []

#             for item in all_node_names:
#                 __nodedata = Nodedata.objects.filter(node_name=item).first()
#                 all_nodeData.append(__nodedata)

#             locations = []
#             all_sensor_data = {nodeName: [] for nodeName in all_node_names}
#             all_latest_sensor_data = []
#             all_latest_5_sensor_data_list = []

#             for node_D in all_nodeData:
#                 locations.append({
#                     'lat': node_D.Loc_lat,
#                     'long': node_D.Loc_long,
#                     'node_name': node_D.node_name
#                 })

#             for __nodeNames in all_node_names:
#                 # print("__nodeNames : ",__nodeNames)

#                 valu = SensorData.objects.filter(
#                     nodename=__nodeNames).order_by('-timestamp')

#                 # print("valu : ", valu)

#                 all_sensor_data[__nodeNames].append(valu)
#                 # values['dadar'].append('Data 1 for Dadar')

#                 # print("all all_sensor_data :", all_sensor_data)

#                 all_latest_sensor_data.append(
#                     SensorData.objects.filter(
#                         nodename=__nodeNames).order_by('-timestamp').first())

#                 ___all_lat_5_sensor_data_list = SensorData.objects.filter(
#                     nodename=__nodeNames).order_by('-timestamp')[:5]
#                 ___all_lat_5_sensor_data_list = ___all_lat_5_sensor_data_list[::
#                                                                               -1]
#                 all_latest_5_sensor_data_list.append(
#                     ___all_lat_5_sensor_data_list)

#             # print("all_latest_5_sensor_data_list :", all_latest_5_sensor_data_list)

#             # user_node_data = Nodedata.objects.filter(node_name=nodename).first()
#             # sensor_data = SensorData.objects.filter(nodename=nodename)

#             # print("locations : ", locations)
#             map_html = get_the_map_multipal_loc(locations)

#         except:
#             all_sensor_data = "null"
#             all_latest_sensor_data = "null"
#             all_latest_5_sensor_data_list = "null"
#             map_html = "null"

#         # print("all_latest_5_sensor_data_list : " , all_latest_5_sensor_data_list)
#         # Pass data to the template
#         context = {
#             # 'username': user_name,
#             'clustername': clustername,
#             # 'lat': lat,
#             # 'long': long,
#             # 'api_key': api_key,
#             'all_sensor_data': all_sensor_data,
#             'all_latest_sensor_data': all_latest_sensor_data,
#             'all_latest_5_sensor_data_list': all_latest_5_sensor_data_list,
#             'map_html': map_html,
#         }
#         return render(request, 'agroapp/clusterdata.html', context)

#     else:
#         context = {"message": "wrong_route"}
#         return render(request, 'agroapp/clusterdata.html', context)




# route : http://127.0.0.1:8000/read_sensor_data/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar


# def read_sensor_data(request):
#     if request.method == 'GET':
#         username = request.GET.get('username', '')
#         api_key = request.GET.get('api_key', '')
#         nodename = request.GET.get('nodename', '')

#         # Validate the username, API key, and nodename
#         user_node_data = Nodedata.objects.filter(user_name=username,
#                                                  api_key=api_key,
#                                                  node_name=nodename).first()

#         if user_node_data:
#             sensor_data = SensorData.objects.filter(nodename=nodename)
#             # Convert QuerySet to a list of dictionaries
#             sensor_data_list = list(sensor_data.values())

#             ret_data = {
#                 'user_name': username,
#                 'node_name': nodename,
#                 'sensor_Data': sensor_data_list,
#             }
#             return JsonResponse(ret_data)
#         else:
#             return JsonResponse({
#                 'status':
#                 'error',
#                 'message':
#                 'Invalid username, API key, or nodename'
#             })

#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })


# route : http://127.0.0.1:8000/sensordata/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar&Depth_1=45.3&Depth_2=49.3&Depth_3=55.9&temperature=55.9&humidity=55.9


# def get_formatted_datetime():
#     # Get the current date and time
#     now = datetime.now()

#     # Add 6 hours to the current time
#     future_time = now + timedelta(hours=6)

#     # Define the month names
#     month_names = [
#         "January", "February", "March", "April", "May", "June", "July",
#         "August", "September", "October", "November", "December"
#     ]

#     # Extract the components of the date and time
#     month = month_names[future_time.month - 1]  # Adjust index to start from 0
#     day = future_time.day
#     year = future_time.year
#     hour = future_time.strftime("%I")  # 12-hour format
#     minute = future_time.minute
#     ampm = future_time.strftime("%p").lower()  # AM or PM

#     # Format the date and time string
#     formatted_date_time = f"{month} {day}, {year}, {hour}:{minute} {ampm}."

#     return formatted_date_time


# # @csrf_exempt
# def sensor_data(request):
#     if request.method == 'GET':
#         # Get parameters from the GET request
#         username = request.GET.get('username', '')
#         api_key = request.GET.get('api_key', '')
#         nodename = request.GET.get('nodename', '')

#         depth_1 = float(request.GET.get('Depth_1', None))
#         depth_2 = float(request.GET.get('Depth_2', None))
#         depth_3 = float(request.GET.get('Depth_3', None))

#         temperature = float(request.GET.get('temperature', None))
#         humidity = float(request.GET.get('humidity', None))

#         timestampManual = get_formatted_datetime()
#         print("timestampManual :", timestampManual)

#         # Validate the username, API key, and nodename
#         user_node_data = Nodedata.objects.filter(user_name=username,
#                                                  api_key=api_key,
#                                                  node_name=nodename).first()

#         if user_node_data:
#             # Save data to the database
#             sensor_data = SensorData(
#                 nodename=nodename,
#                 depth_1=depth_1,
#                 depth_2=depth_2,
#                 depth_3=depth_3,
#                 temperature=temperature,
#                 humidity=humidity,
#                 timestamp=timestampManual  # Set the timestamp manually
#             )
#             sensor_data.save()

#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({
#                 'status':
#                 'error',
#                 'message':
#                 'Invalid username, API key, or nodename'
#             })

#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })


'''
node_prabhadevi
9650ad02-52e0-4825-8f63-ef2b5235ee77

node_dadar
5df155f4-9161-44b9-8ff5-9c821709e1bf
'''
'''
import random

def generate_api_key():
    key_length = 36  # Length of the API key
    dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

    characters = "abcdef0123456789"

    api_key = ''.join(random.choice(characters) if i not in dash_positions else '-' for i in range(key_length))
    return api_key

# Example usage
api_key = generate_api_key()
print(api_key)

'''


# def generate_api_key():
#     key_length = 36  # Length of the API key
#     dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

#     characters = "abcdefghijklmnopqrstwxyz0123456789"

#     api_key = ''.join(
#         random.choice(characters) if i not in dash_positions else '-'
#         for i in range(key_length))
#     return api_key


# def generate_unique_api_key():
#     while True:
#         # api_key = str(uuid.uuid4())
#         api_key = str(generate_api_key())
#         if not Nodedata.objects.filter(api_key=api_key).exists():
#             return api_key


# def your_view_function(request):
#     # Your view logic here
#     api_key = generate_unique_api_key()

#     # Use api_key in your view logic or save it to the database

#     return HttpResponse(f"Generated API Key: {api_key}")


# ------------------------------------
# Sample Code Below
# ------------------------------------

# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n])

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)

# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)

#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })

# # def index(request):
# #     return HttpResponse('Teamzeffort    |      index Page')
