'''
This file is designed to illustrate Python class
'''
class Student:
    """
    This class create a Student data structure,
    which allows us to set and retrieve the course grade for a specific student,
    and calculate the GPA
    """
    def __init__(self, student_id, name, level, grades=None):
        """
        All classes have a function called __init__,
        which is always executed when the class is being initiated.
        Use this function to assign values to object properties,
        or other operations that are necessary to do when the object is being created.

        self represents the instance of the class.
        It allows you to access the attributes and methods of the class in Python

        :param student_id: the student id
        :type student_id: int
        :param name: the student full name
        :type name: str
        :param level: student's program level, i.e., bachelor, master, or phd
        :type level: str
        :param grades: the grade for the spefic class, defaults to None
        :type grades: dict, optional
        """
        self.student_id = student_id
        self.name = name
        self.level = level
        self.grades = grades or {}


    def set_grade(self, course, grade):
        """
        set grade of a course

        :param course: course name
        :type course: str
        :param grade: the grade of the course
        :type grade: float
        """
        self.grades[course] = grade


    def get_grade(self, course):
        """
        retrieve the course grade

        :param course: the course name
        :type course: str
        :return: the grade
        :rtype: float
        """
        return self.grades[course]


    def get_gpa(self):
        """
        calculate the student overall GPA

        :return: the GPA of this student
        :rtype: float
        """
        return sum(self.grades.values())/len(self.grades)


if __name__ == "__main__":
    # let's play with this class
    pass
