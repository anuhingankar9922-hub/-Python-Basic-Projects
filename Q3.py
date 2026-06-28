def manage_marks():
    marks = []

    print("<><><><><> Enter marks of 5 subjects <><><><><>")

    while len(marks) < 5:
        try:
            mark = float(input(f"Enter mark {len(marks)+1}: "))
            marks.append(mark)
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\n><><><><>< Result ><><><><><")
    print("Marks List:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    marks.sort(reverse=True)
    print("\nMarks in Descending Order:", marks)


# Function Call
manage_marks()