from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.http import HttpResponse


# READ: Show all students
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )

def student_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        Student.objects.create(
            name = name,
            email = email,
            age = age
        )

        return redirect("student_list")

    return render(request, "students/student_form.html")

# READ: show one student
def student_detail(request,id):
    student = get_object_or_404(Student, id=id)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )

# UPADTE: edit an existing student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if(request.method == "POST"):
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")

        student.save()

        return redirect("student_list")

    return render(
       request,
       "students/student_form.html",
       {"student": student}
    )    

# DELETE: Delete a student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id),

    if request.method == "POST":
        student.delete()

        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student":student}
    )

