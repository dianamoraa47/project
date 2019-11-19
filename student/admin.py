from django.contrib import admin
from django.contrib.auth.models import User

from.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_displays = ("Registration_number", "First_name","Last_name","Dateofbirth","Email")
	search_fields = (" Registration_number","First_name","Last_name","Email")

 

 

# admin.site.register(Student)

admin.site.register(Student,StudentAdmin)
