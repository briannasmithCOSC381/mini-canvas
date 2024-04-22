from fastapi import FastAPI
from typing import List
from course import CourseManager, Course
from user import UserManager
from fastapi.security import APIKeyHeader

coursemanager = CourseManager()
usermanager = UserManager()
usermanager.create_a_user("John", "pwd", "student")
usermanager.create_a_user("Alice", "pwd", "teacher")
usermanager.create_a_user("Jimmy", "pwd", "admin")

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to our miniCanvas!"

@app.post("/courses/{coursecode}")
def create_a_course(coursecode: str, 
                    semester: str, 
                    teacher_id_list: List[int]) -> int:
    if not coursecode or not semester or not teacher_id_list:
        raise HTTPException(status_code=400, detail="Invalid input: coursecode, semester, and teacher_id_list cannot be empty.")
    
    # Ensure teacher_id_list is a list
    if not isinstance(teacher_id_list, list):
        raise HTTPException(status_code=400, detail="Invalid input: teacher_id_list must be a list.")
    
    # Fetch teachers
    teacher_list = usermanager.find_users(teacher_id_list)
    if not teacher_list:
        raise HTTPException(status_code=404, detail="No teachers found with the provided IDs.")
    
    ### an admin should create a course
    teacher_list = usermanager.find_users(teacher_id_list)
    if not teacher_list:
        raise HTTPException(status_code=404, detail="No teachers found with the provided IDs.")
    
    # Create course
    try:
        course_id = coursemanager.create_a_course(coursecode, semester, teacher_list)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    print(str(course.teacher_list[0]))

    return course_id

@app.put("/courses/{courseid}/students")
def import_students(courseid: int,
                    student_id_list: List[int]) -> None:
    if not student_id_list:
        raise HTTPException(status_code=400, detail="Invalid input: student_id_list cannot be empty.")
    
    # Fetch course
    try:
        course = coursemanager.find_a_course(courseid)
    except CourseNotFoundException:
        raise HTTPException(status_code=404, detail=f"Course with ID {courseid} not found.")
    
    student_list = usermanager.find_users(student_id_list)
    if not student_list:
        raise HTTPException(status_code=404, detail="No students found with the provided IDs.")

    course.import_students(student_list)
    
    print(course.course_id)
    print(course.student_list)
    
    return None