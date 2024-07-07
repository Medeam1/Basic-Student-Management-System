students = {}  # {name: {age: age, grade: grade, subjects: []}}


def student_validation(name, age):
    age_is_valid = False
    name_is_valid = False
    if name.isalpha():
        name_is_valid = True
    if age > 0:
        age_is_valid = True
    if age_is_valid and not name_is_valid:
        print("Please enter a valid name")
        return name_is_valid
    elif not age_is_valid and name_is_valid:
        print("Please enter a valid age")
        return age_is_valid
    return True


def student_exists():
    while True:
        input_name = input("Please enter the name of the student or go back[0]: ")
        if input_name == "0":
            return False, ""
        elif input_name not in students:
            print(f"Name {input_name} not found!")
            continue
        else:
            return True, input_name


def add_student(name: str, age: int, grade: float, subjects: list):
    if student_validation(name, age):
        if name not in students:
            students[name] = {}
        students[name] = {"Age": age, "Grade": grade, "Subjects": subjects}
        return students


def update_student(name: str):

    print("What do you want to update?")
    print("1. Age")
    print("2. Grade")
    print("3. Subjects")
    print("4. Go Back")

    update_choice = input()
    if update_choice == "1":
        old_age = students[name]["Age"]
        while True:
            new_age = int(input(f"Current age is {old_age}. Please enter new age: "))
            if new_age <= 0 or new_age < old_age:
                print("Invalid age!")
                continue
            students[name]["Age"] = new_age
            return f"New age: {new_age}"
    elif update_choice == "2":
        old_grade = students[name]["Grade"]
        while True:
            new_grade = int(input(f"Current grade is {old_grade}. Please enter new grade: "))
            if new_grade <= 1:
                print("Invalid grade!")
                continue
            students[name]["Grade"] = new_grade
            return f"New grade: {new_grade}"

    elif update_choice == "3":
        new_subjects = input("Please enter all subjects separated by ',': ").split(",")
        students[name]["Subjects"] = new_subjects
        return "New subjects:" + '\n'.join(new_subjects)


def delete_student(name):
    del students[name]
    return f"Student {name} successfully deleted!"


def search_student(name):
    result = [name,
              f"Age: {students[name]['Age']}",
              f"Grade: {students[name]['Grade']}",
              f"Subjects: {', '.join(students[name]['Subjects'])}"]
    return '\n'.join(result)


def list_all_students():
    # TypeError to be fixed
    result = []
    for student, info in students.items():
        result.append(f"{student}: ")
        for key, value in info.items:
            result.append(f"-> {key}: {value}")


def main():

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input()
        if choice == "1":
            name = input("Please enter student's name: ")
            age = int(input("Please enter student's age: "))
            while True:
                grade = float(input("Please enter student's grade: "))
                if 2 <= grade <= 6:
                    break
                print("Incorrect grade!")
            subjects = input("Please enter student's grade separated by ',': ").split(",")
            add_student(name,age,grade,subjects)

        elif choice == "2":
            is_valid, name = student_exists()
            if is_valid:
                print(update_student(name))
            else:
                continue

        elif choice == "3":
            is_valid, name = student_exists()
            if is_valid:
                print(delete_student(name))
            else:
                continue

        elif choice == "4":
            is_valid, name = student_exists()
            if is_valid:
                print(search_student(name))
            else:
                continue

        elif choice == "5":
            print(list_all_students())

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
