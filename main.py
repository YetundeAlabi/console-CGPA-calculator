from calculator import CumulativeGradePointAverage

student_cgpa = CumulativeGradePointAverage()
student_cgpa.courses()
print(f"Your semester Grade Point Average is: {student_cgpa.gpa_result()}")
print(f"Your current Cumulative Grade Point Average is: {student_cgpa.result()}")
