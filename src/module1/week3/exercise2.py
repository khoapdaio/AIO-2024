class Person:
	def __init__(self, name, yob):
		self.name = name
		self.yob = yob

	def describe(self):
		return f"Name: {self.name}, Year of Birth: {self.yob}"


class Student(Person):
	def __init__(self, name, yob, grade):
		super().__init__(name, yob)
		self.grade = grade

	def describe(self):
		return f"Student - {super().describe()}, Grade: {self.grade}"


class Teacher(Person):
	def __init__(self, name, yob, subject):
		super().__init__(name, yob)
		self.subject = subject

	def describe(self):
		return f"Teacher - {super().describe()}, Subject: {self.subject}"


class Doctor(Person):
	def __init__(self, name, yob, specialist):
		super().__init__(name, yob)
		self.specialist = specialist

	def describe(self):
		return f"Doctor - {super().describe()}, Specialist: {self.specialist}"


class Ward:
	def __init__(self, name):
		self.name = name
		self.people = []

	def add_person(self, person):
		self.people.append(person)

	def describe(self):
		description = f"Ward: {self.name}\n"
		description += "\n".join([person.describe() for person in self.people])
		return description

	def count_doctor(self):
		return sum(1 for person in self.people if isinstance(person, Doctor))

	def sort_age(self, reverse: bool = False):
		self.people.sort(key = lambda person: person.yob, reverse = reverse)

	def compute_average(self):
		teachers = [person for person in self.people if isinstance(person, Teacher)]
		if not teachers:
			return 0
		total_yob = sum(teacher.yob for teacher in teachers)
		return total_yob / len(teachers)


# Tạo một ward object và thêm người vào ward
ward = Ward("Ward 1")
ward.add_person(Student("Alice", 2005, "10th Grade"))
ward.add_person(Teacher("Mr. Smith", 1980, "Mathematics"))
ward.add_person(Teacher("Ms. Johnson", 1985, "Science"))
ward.add_person(Doctor("Dr. Adams", 1975, "Cardiology"))
ward.add_person(Doctor("Dr. Baker", 1982, "Neurology"))

# In ra thông tin của ward
print(ward.describe())

# Kiểm tra số lượng doctor trong ward
print("Number of Doctors:", ward.count_doctor())

# Sắp xếp mọi người theo tuổi
ward.sort_age(reverse = True)
print("\nAfter sorting by age:")
print(ward.describe())

# Tính trung bình năm sinh của các giáo viên trong ward
average_yob = ward.compute_average()
print("\nAverage Year of Birth of Teachers:", average_yob)
