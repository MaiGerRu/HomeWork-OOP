class Mentor:

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции:{self.grades}"

    def __eq__(self, other):
        return self.grades == other.grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за домашние задания: {self.grades} Курсы в процессе изучения: {self.courses_in_progress}Завершенные курсы: {self.finished_courses}"


    def __eq__(self, other):
        return self.grades == other.grades




best_lecturer = Lecturer('Ruoy', 'Eman')
best_lecturer.courses_in_progress += ['Python']

cool_student = Student('Some', 'Buddy')
cool_student.courses_attached += ['Python']

cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)

print(best_lecturer.grades)


best_student = Student('Ruoy', 'Eman')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

