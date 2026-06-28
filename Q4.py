class Student:
    def __init__(self, name, rollNo):
        self.name=name
        self.roll_no=rollNo
        self.marks_list=[]

    def add_mark(self, mark):
        try:
            mark=float(mark)

            if mark < 0 or mark > 100:
                raise ValueError("Please enter marks between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("Please enter valid marks:", e)

    def get_average(self):
        if len(self.marks_list)==0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("\n--::::: Student Details :::::--")
        print("\nName :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())
        print()

try:
    name=input("\nEnter Student Name: ")
    roll=input("Enter Roll Number: ")

    s1=Student(name, roll)
    print()
    for i in range(5):
        mark=input(f"Enter mark {i+1}: ")
        s1.add_mark(mark)

    s1.display_info()

except Exception as e:
    print("Error:", e)