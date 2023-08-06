'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/grading
'''











def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            # If the grade is less than 38, no rounding occurs
            rounded_grades.append(grade)
        else:
            # Find the next multiple of 5
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            # Check if the difference between the next multiple of 5 and the grade is less than 3
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    return rounded_grades

# Sample Input
num_students = int(input())
grades = []
for i in range(num_students):
    b=int(input())
    grades.append(b)

# Call the function and print the output
rounded_grades = gradingStudents(grades)
for grade in rounded_grades:
    print(grade)
