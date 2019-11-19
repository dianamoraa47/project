from django.urls import path
from .views import add_student
from .views import list_students
from .views import student_details
from .views import edit_student
# from .views import all_students



urlpatterns = [
path("add/", add_student, name = "add_student"),
path("list/", list_students, name = "list_students"),
# path("edit/<int:pk>/",student_details, name ="edit_student"),
# path("view/<int:pk>/", edit_student, name = "student_details"),

path("view/<int:pk>/",student_details, name ="student_details"),
path("edit/<int:pk>/", edit_student, name = "edit_student"),
# path("all/<int:pk>/", all_students, name = "all_students"),


]
