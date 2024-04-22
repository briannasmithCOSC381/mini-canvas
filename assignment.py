class Assignment:
    def __init__(self, assignment_id, due_date, course_id):
        if not assignment_id:
            raise ValueError("Assignment ID cannot be empty")
        if not due_date:
            raise ValueError("Due date cannot be empty")
        if not course_id:
            raise ValueError("Course ID cannot be empty")

        self.assignment_id = assignment_id
        self.due_date = due_date
        self.course_id = course_id
        self.submission_list = []

    def submit(self, submission):
        self.submission_list.append(submission)

class Submission:
    def __init__(self, student_id, content):
        if not student_id:
            raise ValueError("Student ID cannot be empty")
        if not content:
            raise ValueError("Submission content cannot be empty")

        self.student_id = student_id
        self.submission = content
        self.grade = -1.0  # Default grade

    def __str__(self) -> str:
        return f"Submission by student ID {self.student_id}: {self.submission}"

