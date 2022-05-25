def grade_point(grade):
    """it gives point to each grade and return the point"""
    point = 0
    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    return point


student_status = input('Enter student status: "N" for New or "R" for Returning student\n')
num_of_courses = int(input("Enter the number of the current semester courses: "))
total_units = 0
total_points = 0
cumulative_grade_point_average = 0
for course in range(1, num_of_courses + 1):
    units = int(input(f"Enter the units of number {course} course: "))
    grade = input(f"Enter the letter grade: ").upper()
    total_units += units
    score = grade_point(grade) * units
    total_points += score


grade_point_average = round(total_points / total_units, 2)

if student_status == "N".upper():
    cumulative_grade_point_average += round(total_points / total_units, 2)

elif student_status == "R".upper():
    last_semester_total_points = int(input(f"Enter your previous total point: "))
    last_semester_total_units = int(input(f"Enter your previous total units: "))
    total_points += last_semester_total_points
    total_units += last_semester_total_units
    cumulative_grade_point_average = round(total_points / total_units, 2)

print(f"Your semester Grade Point Average is: {grade_point_average }")
print(f"Your current Cumulative Grade Point Average is: {cumulative_grade_point_average }")
