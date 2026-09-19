from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name = "student_list"),
    path("create/", views.student_create, name = "student_create"),
    path("student/<int:id>",views.student_detail, name = "student_detail"),
    path("student/<int:id>/update/", views.student_update, name = "student_update"),
    path("student/<int:id>/delete", views.student_delete, name = "student_delete"),
]
