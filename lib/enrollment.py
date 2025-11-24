class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}   # {enrollment: grade}

    def enroll(self, course, date):
        from .enrollment import Enrollment
        enrollment = Enrollment(self, course, date)
        self._enrollments.append(enrollment)
        return enrollment

    def course_count(self):
        return len(self._enrollments)

    def add_grade(self, enrollment, grade):
        self._grades[enrollment] = grade

    def aggregate_average_grade(self):
        total = sum(self._grades.values())
        num_courses = len(self._grades)
        return total / num_courses

class Course:
    def __init__(self, title):
        self.title = title


from datetime import datetime

class Enrollment:
    all = []

    def __init__(self, student, course, date):
        self.student = student
        self.course = course
        self._date = date
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
