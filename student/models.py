from django.db import models
from course.models import Course
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# from Student.validators import validate_d_email
import datetime

class Student(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name  = models.CharField(max_length = 50)
    Dateofbirth = models.DateField()
    Gender = models.CharField(max_length = 20)
    Registration_number = models.CharField(max_length=5)
    Email = models.EmailField(max_length = 70)
    Phonenumber  = models.CharField(max_length = 12)
    Date_joined  = models.DateField()
    Course = models.ManyToManyField(Course, null=True, blank=True, related_name="student")
    Image = models.ImageField(upload_to='Image',blank=True)
    
    def full_name(self):
        return self.First_name

    def full_name(self):
        return"{} {}".format(self.First_name, self.Last_name)
               
    def __str__(self):  
        return self.First_name+''+self.Last_name

    def take_age():
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


    age = property(take_age)

    def clean(self):
        age = self.age
        if age <17 or age > 30 :
           raise ValidationError("wsdfghjgf")
       # retrun self.cleaned_data()
        return age


    # class Post(models.Model):
    #     # title = models.TextField()
    #     cover = models.ImageField(upload_to='images/')

    # def __str__(self):
    #         return self.title

