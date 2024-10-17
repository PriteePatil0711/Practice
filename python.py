def get_grade(marks):
    """Determine the grade based on marks."""
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def display_students(students):
    """Display all student details."""
    if not students:
        print("No student records found.")
        return
    print("\nStudent Details:")
    for name, details in students.items():
        age = details['age']
        marks = details['marks']
        grade = get_grade(marks)
        print(f"Name: {name}, Age: {age}, Marks: {marks}, Grade: {grade}")

def main():
    """Main function to manage student information."""
    students = {}
    
    while True:
        print("\nStudent Information Management System")
        print("1. Add New Student")
        print("2. Update Existing Student")
        print("3. Display All Students")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            marks = float(input("Enter student marks: "))
            students[name] = {'age': age, 'marks': marks}
            print(f"Student {name} added successfully.")
        
        elif choice == '2':
            name = input("Enter student name to update: ")
            if name in students:
                age = int(input("Enter new age (or press enter to keep current): ") or students[name]['age'])
                marks = input("Enter new marks (or press enter to keep current): ")
                marks = float(marks) if marks else students[name]['marks']
                students[name] = {'age': age, 'marks': marks}
                print(f"Student {name} updated successfully.")
            else:
                print(f"Student {name} not found.")
        
        elif choice == '3':
            display_students(students)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()