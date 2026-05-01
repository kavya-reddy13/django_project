
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher

# TEACHER CRUD

def teacher_list(request):
    data = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'data': data})

def teacher_add(request):
    if request.method == 'POST':
        Teacher.objects.create(
            name=request.POST['name'],
            subject=request.POST['subject'],
            email=request.POST['email'],
            experience=request.POST['experience'],
            phone=request.POST['phone'],
            address=request.POST['address'],
        )
        return redirect('/teacher/')
    return render(request, 'teacher_form.html')

def teacher_edit(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.name = request.POST['name']
        teacher.subject = request.POST['subject']
        teacher.email = request.POST['email']
        teacher.experience = request.POST['experience']
        teacher.phone = request.POST['phone']
        teacher.address = request.POST['address']
        teacher.save()
        return redirect('/teacher/')

    return render(request, 'teacher_form.html', {'teacher': teacher})

def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('/teacher/')