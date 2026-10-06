from django.shortcuts import render
from .models import Course,Message

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Message.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, "contact.html")

def course_detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, "course_detail.html", {"course": course})