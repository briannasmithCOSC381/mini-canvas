import unittest
from user import UserManager, User
from course import CourseManager, Course
from assignment import Assignment, Submission


class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.usermanager = UserManager()
        self.usermanager.create_a_user("Brianna", "pwd", "student")
        self.usermanager.create_a_user("Allen", "pwd", "teacher")
        self.usermanager.create_a_user("Carolina", "pwd", "admin")

    def test_generate_id(self):
        # Arrange
        expected_id = 4

        # Act
        generated_id = self.usermanager.generate_id()

        # Assert
        self.assertEqual(generated_id, expected_id)

    def test_create_a_user(self):
        # Arrange
        initial_user_count = len(self.usermanager.user_list)
        new_user_name = "TestUser"
        new_user_type = "student"

        # Act
        self.usermanager.create_a_user(new_user_name, "pwd", new_user_type)
        updated_user_count = len(self.usermanager.user_list)

        # Assert
        self.assertEqual(updated_user_count, initial_user_count + 1)
        self.assertEqual(self.usermanager.user_list[-1].name, new_user_name)
        self.assertEqual(self.usermanager.user_list[-1].type, new_user_type)

    def test_find_users(self):
        # Arrange
        user_ids_to_find = [1, 2]
        expected_user_names = ["Brianna", "Allen"]

        # Act
        found_users = self.usermanager.find_users(user_ids_to_find)

        # Assert
        self.assertEqual(len(found_users), len(user_ids_to_find))
        for i, user in enumerate(found_users):
            self.assertEqual(user.name, expected_user_names[i])

class TestCourseManager(unittest.TestCase):
    def setUp(self):
        self.course_manager = CourseManager()

    def test_create_a_course_valid_input(self):
        # Valid input: non-empty course code, semester, and teacher list
        course_code = "COSC381"
        semester = "Winter 2024"
        teacher_list = ["Allen Ma", "Brianna Smith"]
        
        # Create a new course
        course_id = self.course_manager.create_a_course(course_code, semester, teacher_list)

        # Verify that the course was created successfully
        self.assertTrue(course_id > 0)  # Course ID should be a positive integer
        self.assertEqual(len(self.course_manager.course_list), 1)  # Course list should contain one course

    def test_create_a_course_invalid_input(self):
        # Invalid input: empty course code
        course_code = ""
        semester = "Winter 2024"
        teacher_list = ["Allen Man", "Brianna Smith"]

        # Verify that ValueError is raised
        with self.assertRaises(ValueError):
            self.course_manager.create_a_course(course_code, semester, teacher_list)

        # Invalid input: empty semester
        course_code = "COSC381"
        semester = ""
        teacher_list = ["Allen Ma", "Brianna Smith"]

        # Verify that ValueError is raised
        with self.assertRaises(ValueError):
            self.course_manager.create_a_course(course_code, semester, teacher_list)

        # Invalid input: empty teacher list
        course_code = "COSC381"
        semester = "Winter 2024"
        teacher_list = []

        # Verify that ValueError is raised
        with self.assertRaises(ValueError):
            self.course_manager.create_a_course(course_code, semester, teacher_list)

        # Invalid input: teacher list is not a list
        course_code = "COSC381"
        semester = "Winter 2024"
        teacher_list = "Allen Ma"  # Not a list

        # Verify that ValueError is raised
        with self.assertRaises(ValueError):
            self.course_manager.create_a_course(course_code, semester, teacher_list)

        # Invalid input: teacher name in the list is not a string
        course_code = "COSC381"
        semester = "Winter 2024"
        teacher_list = ["Allen Ma", 123]  # Int instead of string

        # Verify that ValueError is raised
        with self.assertRaises(ValueError):
            self.course_manager.create_a_course(course_code, semester, teacher_list)

        # Invalid input: teacher name in the list is an empty string
        course_code = "COSC381"
        semester = "Winter 2024"
        teacher_list = ["Allen Ma", ""]  # Empty string

        # Verify that ValueError is raised
        with self.assertRaises(ValueError):
            self.course_manager.create_a_course(course_code, semester, teacher_list)


class TestCourse(unittest.TestCase):
    def setUp(self):
        self.teacher_list = [User(1, "Jinyoung", "pwd", "teacher")]
        self.student_list = [User(2, "Jihyo", "pwd", "student")]
        self.course = Course(1, "COSC381", "Winter", self.teacher_list)

    def test_import_students(self):
        # Arrange
        initial_student_count = len(self.course.student_list)

        # Act
        self.course.import_students(self.student_list)
        updated_student_count = len(self.course.student_list)

        # Assert
        self.assertEqual(updated_student_count, initial_student_count + len(self.student_list))
        self.assertEqual(self.course.student_list[-1].name, "Jihyo")

    def test_create_an_assignment(self):
        # Arrange
        initial_assignment_count = len(self.course.assignment_list)
        due_date = "2024-04-21"

        # Act
        self.course.create_an_assignment(due_date)
        updated_assignment_count = len(self.course.assignment_list)

        # Assert
        self.assertEqual(updated_assignment_count, initial_assignment_count + 1)

if __name__ == "__main__":
    unittest.main()