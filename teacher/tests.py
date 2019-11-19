from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm


import datetime
class TeacherTestCase(TestCase):
   def setUp(self):
       self.teacher = Teacher(
    First_name ="diana"
	Last_name  ="moraa"
	TAC_number =" 244"
	Subject ="english"
	KRA_PIN = "90"
	Gender ="female"
	Registration_number = "2345"
	Email ="dmoraa@gmail.com"
	Phonenumber  ="0728732423"
	Profession ="andriod dev"
	Date_employed = datetime.date.today(),
           )
   def setUp(self):
       self.data = {
                     "First_name":"Harry",
					 "Last_name":"Kane",
					 "TAC_number ":"543",
			         "Subject":"life skills",
			         "Registration_number":"5463",
			         "Email":"angelkanem@gmail.com",
			         "Phonenumber":"0794848934",
			         "Profession":"software engineer",
			          Date_joined :datetime.date.today,
       }
       self.bad_data ={
                      "First_name":"Harry",
					 "Last_name":"Kane",
					 "TAC_number ":"543",
			         "Subject":"life skills",
			         "Registration_number":"5463",
			         "Email":"angelkanem@gmail.com",
			         "Phonenumber":"0794848934",
			         "Profession":"software engineer",
			          Date_joined :datetime.date.today,
       }
   def test_teacher_form_accepts_valid_data(self):
       form = TeacherForm(self.data)
       self.assertTrue(form.is_valid())
   def test_teacher_form_rejects_invalid_data(self):
       form = TeacherForm(self.bad_data)
       self.assertFalse(form.is_valid())



				
# Create your tests here.
