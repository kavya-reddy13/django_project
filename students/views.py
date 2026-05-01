
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('/login/')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    return render(request, 'dashboard.html')


# STUDENT CRUD

def student_list(request):
    data = Student.objects.all()
    return render(request, 'student_list.html', {'data': data})

def student_add(request):
    if request.method == 'POST':
        Student.objects.create(
            first_name=request.POST['first_name'],
            middle_name=request.POST['middle_name'],
            last_name=request.POST['last_name'],
            course=request.POST['course'],
            gender=request.POST['gender'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        return redirect('/students/')
    return render(request, 'student_form.html')

def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.middle_name = request.POST['middle_name']
        student.last_name = request.POST['last_name']
        student.course = request.POST['course']
        student.gender = request.POST['gender']
        student.phone = request.POST['phone']
        student.address = request.POST['address']
        student.email = request.POST['email']
        student.password = request.POST['password']
        student.save()
        return redirect('/students/')

    return render(request, 'student_form.html', {'student': student})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/students/')