class GradePointAverage:

    def __init__(self):
        self.num_of_courses = int(input("Enter the number of the current semester courses: "))
        self.total_units = 0
        self.total_points = 0
        self.point = 0
        print("\n")

    def courses(self):
        for course in range(1, self.num_of_courses + 1):
            units = int(input(f"Enter the units of number {course} course: "))
            grade = input(f"Enter the letter grade: ").upper()
            print("\n")
            self.total_units += units
            score = self.grade_point(grade) * units
            self.total_points += score

    def grade_point(self, grade):
        """it gives point to each grade and return the point"""
        if grade == "A":
            self.point = 5
        elif grade == "B":
            self.point = 4
        elif grade == "C":
            self.point = 3
        elif grade == "D":
            self.point = 2
        elif grade == "E":
            self.point = 1
        return self.point

    def gpa_result(self):
        grade_point_average = round(self.total_points / self.total_units, 2)
        return grade_point_average


class CumulativeGradePointAverage(GradePointAverage):
    def __init__(self):
        super().__init__()
        self.previous_total_points = int(input(f"Enter your previous total points: "))
        print("\n")
        self.previous_total_units = int(input(f"Enter your previous total units: "))
        print("\n")

    def result(self):
        self.total_points += self.previous_total_points
        self.total_units += self.previous_total_units
        cumulative_grade_point_average = round(self.total_points / self.total_units, 2)
        return cumulative_grade_point_average

