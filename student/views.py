from django.shortcuts import render, redirect
from .models import Student


def index(request):
    data = Student.objects.all()
    return render(request, "index.html", {"students": data})


def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        usn = request.POST['usn']
        sem = request.POST['sem']
        branch = request.POST['branch']

        Student.objects.create(
            name=name,
            usn=usn,
            sem=sem,
            branch=branch
        )

        return redirect('/')

    return render(request, "add.html")


def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.usn = request.POST['usn']
        student.sem = request.POST['sem']
        student.branch = request.POST['branch']

        student.save()

        return redirect('/')

    return render(request, "update.html", {"student": student})


def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')