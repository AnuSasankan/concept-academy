from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("courses/", views.courses, name="courses"),
    path("contact/", views.contact, name="contact"),
    path("courses/<int:id>/", views.course_detail, name="course_detail"),
]

urlpatterns += staticfiles_urlpatterns()