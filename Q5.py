def student_database():
    students = {}

    while True:
        print("\n---<>--- Student Database Menu ---<>---")
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                roll_no = input("\nEnter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll_no: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student added successfully.")

            elif choice == 2:
                roll_no = input("Enter Roll Number to Search: ")

                student = students.get(roll_no)

                if student:
                    print("\nStudent Details")
                    print("Name :", student["Name"])
                    print("Age :", student["Age"])
                    print("City :", student["City"])
                else:
                    print("Student not found.")

            elif choice == 3:
                if len(students) == 0:
                    print("No student records found.")
                else:
                    print("\nAll Student Records")
                    for roll_no, details in students.items():
                        print("-------------------------")
                        print("Roll No :", roll_no)
                        print("Name :", details["Name"])
                        print("Age :", details["Age"])
                        print("City :", details["City"])

            elif choice == 4:
                print("\nExiting Program...")
                print()
                break
                
            else:
                print("\nInvalid choice. Please select between 1 and 4.")

        except ValueError:
            print("\nInvalid input! Please enter a valid number.")


student_database()