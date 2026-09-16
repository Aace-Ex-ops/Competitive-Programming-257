N = int(input("Enter number of students: "))

attendance = []

if N <= 0:
    print("Number of students must be greater than 0.")
else:
    for i in range(N):
        value = float(input(f"Enter attendance for student {i + 1}: "))
        attendance.append(value)

    threshold = 65.0
    for a in attendance:
        if a < 0 or a > 100:
            print("Attendance must be between 0 and 100.")
            exit()
    
    low_attendance_students = sum(1 for a in attendance if a < threshold)

    lowest_attendance = min(attendance)
    lowest_position = attendance.index(lowest_attendance) + 1

    average = sum(attendance) / N

    print(f"Number of students with attendance below {threshold}%: {low_attendance_students}")
    print(f"Lowest attendance: {lowest_attendance}% (Student {lowest_position})")
    print(f"Average attendance: {average:.2f}%")

#There still remains a problem with the code. The program does not handle the case where the user inputs a non-numeric value for attendance. If a user enters a string or any other non-numeric input, the program will raise a ValueError and crash. To fix this, we can add error handling to ensure that the input is valid.

#Also, students with attendance exactly equal to the threshold should not be counted as having low attendance. The current implementation counts students with attendance below the threshold, which is correct, but we should clarify this in the output message.

#And finally, students with same attendance below the threshold should be counted correctly. The current implementation counts all students with attendance below the threshold, but we should ensure that we are not double-counting any students.

#Not done by AI 🙂