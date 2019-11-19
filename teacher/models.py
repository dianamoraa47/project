from django.db import models

class Teacher(models.Model):
	First_name = models.CharField(max_length=50)
	Last_name  = models.CharField(max_length = 50)
	TAC_number = models.CharField(max_length = 15)
	Subject = models.CharField(max_length = 23)
	KRA_PIN = models.CharField(max_length = 20)
	Gender = models.CharField(max_length = 20)
	Registration_number = models.CharField(max_length=5)
	Email = models.EmailField(max_length = 70)
	Phonenumber  = models.CharField(max_length = 12)
	Profession = models.CharField(max_length = 15)
	Date_employed = models.DateField(max_length = 10, null=True)
	def __str__(self):
		return self.First_name+''+self.Last_name

# Create your models here.
