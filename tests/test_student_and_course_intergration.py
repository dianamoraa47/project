from django test import TestCase
from django.models import Student
from django.models import Course
import datetime

class StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a = Student.objects.create(
           First_name = "Diana",
           last_name = "Moraa",
           Dateofbirth = datetime.date(2000,4,9),
           Gender = "female",
           Registration_number = "3411",
           Email = "dianamoraa47@gmail.com",
           Phone_number = "0710950673",
           Date_joined = datetime.date.today(),
           )
		self.student_b = Student.objects.create(
           First_name = "Chris",
           last_name = "Pratt",
           Dateofbirth = datetime.date(1978,2,7),
           Gender = "male",
           Registration_number = "3456",
           Email = "chrispratt@gmail.com",
           Phone_number = "077833728",
           Date_joined = datetime.date.today(),
           )
		self.python = Course.add(
			Name = "Django",
			Duration ="216 days",
			Months = "8",
			Startdate =datetime.date.today(),,
			Enddate =datetime.date.today(),,
			Description ="dealing with database and api's",
			Teacher = "James Mwai"
			)
		self.javasript = Course.add(
			Name = "React",
			Duration ="116 days",
			Months = "7",
			Startdate =datetime.date.today(),,
			Enddate =datetime.date.today(),,
			Description ="js is cool when creating a respomsive website",
			Teacher = "Anthony Orenge"
			)
		self.design = Course.add(
			Name = "Adobe Illustrator",
			Duration ="107 days",
			Months = "5",
			Startdate =datetime.date.today(),,
			Enddate =datetime.date.today(),,
			Description ="mostly deals with sketches and color",
			Teacher = "Nyandia"
			)
		self.design = Course.add(
			Name = "HTML/CSS",
			Duration ="107 days",
			Months = "5",
			Startdate =datetime.date.today(),,
			Enddate =datetime.date.today(),,
			Description ="mostly deals with sketches and color",
			Teacher = "Jeff"
			)
		self.design = Course.add(
			Name = "Hardware electronics",
			Duration ="107 days",
			Months = "5",
			Startdate =datetime.date.today(),,
			Enddate =datetime.date.today(),,
			Description ="mostly deals with sketches and color",
			Teacher = "Barre"
			)
		def test_student_can_join_a_course(self);
			self.student_a.course.add(self.python)
			self.assertEqual(self.student_a.course.count(),1)
			self.student_a.course.add(self.javasript)
			self.assertEqual(self.student_a.course.count(),2)
			self.student_a.course.add(self.design)
			self.assertEqual(self.student_a.course.count(),3)


		def test_student_can_join_many_courses(self):
			self.student_b_courses.add(self.python, self.javasript, self.design)
			self.assertEqual(self.student_b.course.count(),3)


