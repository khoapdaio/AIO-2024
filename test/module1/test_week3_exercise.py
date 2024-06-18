import unittest

import torch

from src.module1.week3.exercise1 import Softmax, SoftmaxStable
from src.module1.week3.exercise2 import Person, Student, Teacher, Doctor, Ward
from src.module1.week3.exercise3 import MyStack
from src.module1.week3.exercise4 import MyQueue


class TestWeek3(unittest.TestCase):
	def setUp(self):
		self.softmax = Softmax()
		self.softmax_stable = SoftmaxStable()
		self.stack = MyStack(3)
		self.queue = MyQueue(3)

		self.ward = Ward("Ward A")
		self.student = Student("Student One", 2005, "B")
		self.teacher1 = Teacher("Teacher One", 1980, "Science")
		self.teacher2 = Teacher("Teacher Two", 1990, "History")
		self.doctor1 = Doctor("Doctor One", 1975, "Dermatology")
		self.doctor2 = Doctor("Doctor Two", 1985, "Neurology")
		self.ward.add_person(self.student)
		self.ward.add_person(self.teacher1)
		self.ward.add_person(self.teacher2)
		self.ward.add_person(self.doctor1)
		self.ward.add_person(self.doctor2)

	def test_invalid_input(self):
		with self.assertRaises(ValueError):
			self.softmax(torch.tensor([[1.0, 2.0], [3.0, 4.0]]))
		with self.assertRaises(ValueError):
			self.softmax_stable(torch.tensor([[1.0, 2.0], [3.0, 4.0]]))

	def test_softmax_output(self):
		x = torch.tensor([1.0, 2.0, 3.0])
		output = self.softmax(x)
		expected_output = torch.exp(x) / torch.sum(torch.exp(x))
		self.assertTrue(torch.allclose(output, expected_output, atol = 1e-6))

	def test_softmax_stable_output(self):
		x = torch.tensor([1.0, 2.0, 3.0])
		output_stable = self.softmax_stable(x)
		max_x = torch.max(x)
		expected_output_stable = torch.exp(x - max_x) / torch.sum(torch.exp(x - max_x))
		self.assertTrue(torch.allclose(output_stable, expected_output_stable, atol = 1e-6))

	def test_consistency_between_methods(self):
		x = torch.tensor([1.0, 2.0, 3.0])
		output = self.softmax(x)
		output_stable = self.softmax_stable(x)
		self.assertTrue(torch.allclose(output, output_stable, atol = 1e-6))

	def test_large_values(self):
		x = torch.tensor([1000.0, 1001.0, 1002.0])
		output_stable = self.softmax_stable(x)
		max_x = torch.max(x)
		expected_output_stable = torch.exp(x - max_x) / torch.sum(torch.exp(x - max_x))
		self.assertTrue(torch.allclose(output_stable, expected_output_stable, atol = 1e-6))

	def test_is_empty(self):
		self.assertTrue(self.stack.is_empty())
		self.stack.push(1)
		self.assertFalse(self.stack.is_empty())

	def test_is_full(self):
		self.assertFalse(self.stack.is_full())
		self.stack.push(1)
		self.stack.push(2)
		self.stack.push(3)
		self.assertTrue(self.stack.is_full())

	def test_push(self):
		self.stack.push(1)
		self.assertEqual(self.stack.top(), 1)
		self.stack.push(2)
		self.assertEqual(self.stack.top(), 2)
		self.stack.push(3)
		self.assertEqual(self.stack.top(), 3)
		with self.assertRaises(OverflowError):
			self.stack.push(4)

	def test_pop(self):
		self.stack.push(1)
		self.stack.push(2)
		self.stack.push(3)
		self.assertEqual(self.stack.pop(), 3)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.pop(), 1)
		with self.assertRaises(IndexError):
			self.stack.pop()

	def test_top(self):
		with self.assertRaises(IndexError):
			self.stack.top()
		self.stack.push(1)
		self.assertEqual(self.stack.top(), 1)
		self.stack.push(2)
		self.assertEqual(self.stack.top(), 2)
		self.stack.pop()
		self.assertEqual(self.stack.top(), 1)

	def test_queue_is_empty(self):
		self.assertTrue(self.queue.is_empty())
		self.queue.enqueue(1)
		self.assertFalse(self.queue.is_empty())

	def test_queue_is_full(self):
		self.assertFalse(self.queue.is_full())
		self.queue.enqueue(1)
		self.queue.enqueue(2)
		self.queue.enqueue(3)
		self.assertTrue(self.queue.is_full())

	def test_enqueue(self):
		self.queue.enqueue(1)
		self.assertEqual(self.queue.front(), 1)
		self.queue.enqueue(2)
		self.assertEqual(self.queue.front(), 1)
		self.queue.enqueue(3)
		self.assertEqual(self.queue.front(), 1)
		with self.assertRaises(OverflowError):
			self.queue.enqueue(4)

	def test_dequeue(self):
		self.queue.enqueue(1)
		self.queue.enqueue(2)
		self.queue.enqueue(3)
		self.assertEqual(self.queue.dequeue(), 1)
		self.assertEqual(self.queue.dequeue(), 2)
		self.assertEqual(self.queue.dequeue(), 3)
		with self.assertRaises(IndexError):
			self.queue.dequeue()

	def test_front(self):
		with self.assertRaises(IndexError):
			self.queue.front()
		self.queue.enqueue(1)
		self.assertEqual(self.queue.front(), 1)
		self.queue.enqueue(2)
		self.assertEqual(self.queue.front(), 1)
		self.queue.dequeue()
		self.assertEqual(self.queue.front(), 2)

	def test_person_describe(self):
		person = Person("John Doe", 1990)
		self.assertEqual(person.describe(), "Name: John Doe, Year of Birth: 1990")

	def test_student_describe(self):
		student = Student("Jane Doe", 2000, "A")
		self.assertEqual(student.describe(), "Student - Name: Jane Doe, Year of Birth: 2000, Grade: A")

	def test_teacher_describe(self):
		teacher = Teacher("Alice Smith", 1985, "Math")
		self.assertEqual(teacher.describe(), "Teacher - Name: Alice Smith, Year of Birth: 1985, Subject: Math")

	def test_doctor_describe(self):
		doctor = Doctor("Bob Brown", 1975, "Cardiology")
		self.assertEqual(doctor.describe(), "Doctor - Name: Bob Brown, Year of Birth: 1975, Specialist: Cardiology")

	def test_add_person(self):
		ward = Ward("Ward B")
		ward.add_person(self.student)
		self.assertEqual(len(ward.people), 1)
		self.assertEqual(ward.people.index(self.student), 0)

	def test_describe(self):
		description = self.ward.describe()
		self.assertIn("Ward: Ward A", description)
		self.assertIn("Student - Name: Student One, Year of Birth: 2005, Grade: B", description)
		self.assertIn("Teacher - Name: Teacher One, Year of Birth: 1980, Subject: Science", description)
		self.assertIn("Teacher - Name: Teacher Two, Year of Birth: 1990, Subject: History", description)
		self.assertIn("Doctor - Name: Doctor One, Year of Birth: 1975, Specialist: Dermatology", description)
		self.assertIn("Doctor - Name: Doctor Two, Year of Birth: 1985, Specialist: Neurology", description)

	def test_count_doctor(self):
		self.assertEqual(self.ward.count_doctor(), 2)

	def test_sort_age(self):
		self.ward.sort_age()
		self.assertEqual(self.ward.people[0], self.doctor1)
		self.assertEqual(self.ward.people[-1], self.student)
		self.ward.sort_age(reverse = True)
		self.assertEqual(self.ward.people[0], self.student)
		self.assertEqual(self.ward.people[-1], self.doctor1)

	def test_compute_average(self):
		average_yob = self.ward.compute_average()
		self.assertEqual(average_yob, (1980 + 1990) / 2)