from django.contrib import admin

from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_displays = ("Registration_number", "First_name","Last_name","Gender","KRA PIN")
	search_fields = (" Registration_number","First_name","Last_name","Gender","KRA PIN")

 

admin.site.register(Teacher,TeacherAdmin)

# Register your models here.
