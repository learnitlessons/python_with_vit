# Basic student record: (student_id, name, major, enrollment_year)
student_record = (20241001, "James Wilson", "Computer Science", 2024)
transfer_student = (20241002, "Sarah Chen", "Data Science", 2024)

# Semester courses: nested tuples with (course_id, name, credits, max_capacity)
course_listing = (
    ("CS101", "Introduction to Programming", 3, 30)
    ("DS201", "Data Analysis Fundamentals", 4, 25)
    ("CS205", "Database Sysstems", 3, 28)
)

# Accessing tuple elements
student_id = student_record[0]
student_name = student_record[1]

# Using tuple unpacking for cleaner code
id_num, name, major, year = student_record
print(f"Sudents: {name}, Major: {major}")

# Count and index methods
programming_students = course_listing.count(("CS101", "Introduction to Programming", 3, 30))
data_course_position = course_listing.index(("DS201", "Data Analysis Fundamentals", 4, 25))

# Mixing with lists and dictionaries
enrollment_changes = [
    ("ADD", ("CS101", "James Wilson", "Fall 2024")),
    ("DROP", ("DS201", "Sarah Chen", "Fall 2024"))
]

department_courses = {
    "Computer Science": ("CS101", "CS205", "CS301"),
    "Data Sciences": ("DS201", "DS205", "DS301")
}

# Grade record: (student_id, course_id, grade, semester)
grade_redords = (
    (20241001, "CS101", "A", "Fall 2024"),
    (20241002, "CS101", "B+", "Fall 2024"),
    (20241003, "CS101", "A-", "Fall 2024")
)

# Current and maximum enrollment comparision
current_enrollment = (28, 22, 25)
max_capacity = (30, 25, 28)

if current_enrollment < max_capacity:
    print("Seats still available in courses")

# Creating waitlist entries
# waitlist_entry = (student_id, course_id, "2025-01-10")

try:
    student_id[1] = "Update name"
except TypeError as e:
    print("Student records cannot be modified after creation")

# Course enrollment tracking
current_enrollment = (
    ("CS101", 28, "Near Capacity"),
    ("DS201", 22, "Available"),
    ("CS205", 25, "Available")
)
enrollment_list = list(current_enrollment)
updated_enrollments = tuple(enrollment_list)

# Course schedule entries: (course_id, day, start_time, end_time, room)

course_schedule = (
    ("CS101", "Monday", "09:00", "10:30", "Room 401"),
    ("DC201", "Tuesday", "11:00", "12:30", "Room 405")
)