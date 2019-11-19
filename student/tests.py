from django.urls import reverse
from django.test import Client
from django.test import TestCase
from .models import Student
from student.forms import StudentForm
import datetime

class StudentTestCase(TestCase):
   def setUp(self):
       self.student = Student(
           First_name = "Diana",
           last_name = "Moraa",
           Dateofbirth = datetime.date(2000,4,9),
           Gender = "female",
           Registration_number = "1234",
           Email = "dianamoraa47@gmail.com",
           Phone_number = "0710950673",
           Date_joined = datetime.date.today(),
           )
    def test_full_name_contains_First_name(self):
		self.assertIn(self.student.First_name, self.student.fullname())

 	def test_full_name_contains_Last_name(self):
 		self.assertIn(self.student.Last_name, self.student.fullname())

 	def test_full_name_contains_name(self):
 		self.assertEqual(result, “Diana Moraa”)

  
class AddStudentTestCase(TestCase):
    def setUp(self):
       self.data = {
       "First_name": "diana",
       "Last_name": "moraa",
       "Dateofbirth": datetime.date(1996,9,4,),
       "Gender": "Female",
       "Registration_number": "3456",
       "Email": "zoya@gmail.com",
       "Phone_number": "0752705031",
       "Date_joined": datetime.date.today(),
       }
       self.bad_data ={
       "First_name": "Diana",
       "Last_name": "moraa",
       "Date_of_birth": datetime.date(1996,9,4),
       "Gender": "Female",
       "Registration_number": "3456",
       "Email": "dianamoraa@gmail.com",
       "Phone_number": "0752705031",
       "Date_joined": datetime.date.today(),
       }
    def test_student_form_accepts_valid_data(self):
       form = StudentForm(self.data)
       self.assertTrue(form.is_valid())
    def test_student_form_rejects_invalid_data(self):
       form = StudentForm(self.bad_data)
       self.assertFalse(form.is_valid())


    def test_add_student_view(self):
    	client = Client()
    	url = reverse("add_student")
    	response = client.post(url,data)
    	self.assertEqual(response.status_code, 200)































































































# from django.test import TestCase
# from .models import Student
# import datetime
# from django.core import validators
# from studentforms import StudentForm
# ximport unittest

# class StudentTestCase(TestCase):
# 	def setUp(self):
# 		self.student=Student(
# 			First_name="Diana",
# 			Last_name="Moraa",
# 			Dateofbirth=datetime.date(2017,7,1),
# 			Gender="female",
# 			Registration_number="3456",
# 			Email="dianamoraa@gmail.com",
# 			Phonenumber="073437436",
# 			Date_joined =datetime.date.today,
# 			)

# 	def test_full_name_contains_First_name(self):
# 		self.assertIn(self.student.First_name, self.student.fullname())

# 	def test_full_name_contains_Last_name(self):
# 		self.assertIn(self.student.Last_name, self.student.fullname())

# 	def test_full_name_contains_name(self):
# 		self.assertEqual(result, “Diana Moraa”)

# class AddStudentTextCase(TextCase):
# 	def setUp(self):
# 		self.data = {"First_Name":"diana",
# 					 "Last_Name":"moraa",
# 					  "Dateofbirth":datetime.date(2017,7,1),
# 			         "Gender":"female",
# 			         "Registration_number":"3456",
# 			         "Email":"dianamoraa@gmail.com",
# 			         "Phonenumber":"073437436",
# 			          Date_joined : datetime.date.today,
# 					}  

# 	def test_student_form_accepts_valid_data(self):
# 		form = StudentForm(self.data)
# 		self.assertTrue(form.is_valid())	



# class AddStudentTextCase(TextCase):
# 	def setUp(self):
# 		self.data = {"First_Name":"Lee",
# 					 "Last_Name":"jet",
# 					  "Dateofbirth":datetime.date(2014,7,1),,
# 			         "Gender":"Male",
# 			         "Registration_number":"23312",
# 			         "Email":"lejet@gmail.com",
# 			         "Phonenumber":"079494392",
# 			          Date_joined :datetime.date.today,
# 					}  					    
# 	def test_student_form_reject_invalid_data(self):
# 		form = StudentForm(self.bad_data)
# 		self.assertFalse(form.is_valid())	

				


# if __name__ == '__main__':
#     unittest.main()


    # class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('diana'.upper(), 'DIANA')

#     def test_isupper(self):
#         self.assertTrue('DIANA'.isupper())
#         self.assertFalse('Diana'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#        main()			

	




# class MyFirstTests(unittest.TestCase):
# 	def test_hello(self):  
# 			self.assertEqual(diana_moraa(), 'diana moraa')      
# 			  def test_custom_num_list(self): 
# 			  	  self.assertEqual(len(create_num_list(10)), 10)

	
			

# # Create your tests here.




# self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string