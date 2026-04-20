import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="om123",
    database="student_db"
)

cursor = conn.cursor()

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(sql, values)
    conn.commit()

    print("Student Added Successfully")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    print("\nStudent Records:")
    print("-------------------------------")

    for row in records:
        print(row)


# Update Student
def update_student():
    student_id = int(input("Enter Student ID to update: "))

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")

    sql = """
    UPDATE students
    SET name=%s, age=%s, course=%s
    WHERE id=%s
    """

    values = (name, age, course, student_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Student Updated Successfully")


# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    sql = "DELETE FROM students WHERE id=%s"

    cursor.execute(sql, (student_id,))
    conn.commit()

    print("Student Deleted Successfully")


# Search Student
def search_student():
    student_id = int(input("Enter Student ID to search: "))

    sql = "SELECT * FROM students WHERE id=%s"

    cursor.execute(sql, (student_id,))

    record = cursor.fetchone()

    if record:
        print("Student Found:", record)
    else:
        print("Student Not Found")


# Menu System
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        search_student()

    elif choice == "6":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")