class Student():

    valid_courses = {"Computer Science", "Software Engineering", "Networks and Security", 
                     "Data Science", "Cybersecurity", "Computing"}
    year = {1, 2, 3, 4}

    def __init__(self, up_number):
        self._up_number = up_number
        self._course = ""
        self._current_year = 1

    @property    
    def course(self):
        return self._course

    @property
    def current_year(self):
        return self._current_year

    @course.setter
    def course(self, new_course):
        if new_course in self.valid_courses:
            self._course = new_course
        else:
            print(f"Invalid course. Valid Courses: {self.valid_courses}.")

    @property
    def upnumber(self):
        return self._up_number

    def progress(self):
        if self._current_year < 4:
            self._current_year += 1
            if self._current_year == 3:
                company = input(f"Enter placement company ({PlacementStudent.company_options}): ")
                if company in PlacementStudent.company_options:
                    return PlacementStudent(self._up_number, company)
                else:
                    print("Invalid company, staying as a regular student.")
        else:
            print("Student has already completed the final year.")
        return self  

    def __str__(self):
        return f"Student {self._up_number} studying {self.course} in year {self.current_year}"


class PlacementStudent(Student):
    
    company_options = {"Google", "Microsoft", "Biggest Data", "Printer"}

    def __init__(self, up_number, company):
        super().__init__(up_number)
        self._current_year = 3
        self.company = company

    def __str__(self):
        return f"Placement student {self._up_number} working at {self.company}"


def StudentTest():
    student_1 = Student("up123")
    student_1.course = "Cybersecurity"
    
    print(student_1)

    student_1.progress()
    print(student_1)

    student_1.course = "Software Engineering"
    student_1 = student_1.progress()
    print(student_1)

    student_1.progress()
    print(student_1)

    student_1.progress()
    print(student_1)

