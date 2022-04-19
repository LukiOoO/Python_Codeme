
import unittest
from student import Student


class Student_tesCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("&&&&setUp****")
        self.st = Student("Anna", "Kowalska", 4.6, None)

    def setUpClass(cls) -> None:


    def test_student_email_created(self):
        st = Student("Anna", "Kowalska", 4.6, None)

        self.assertEqual(st.email, "anna.kowalska@university.com")

    def test_student_email_updated(self):
        st = Student("Anna", "Kowalska", 4.6, None)

        self.assertEqual(st.email, "anna.kowalska@university.com")
        st.last = "smith"
        self.assertEqual(st.email, "anna.smith@university.com")


    def test_student_grant_schollarship(self):
        stB = Student("Bartosz", "Borowik", 3.6, None)

        self.S



if __name__ == "__main__":
    unittest.main()