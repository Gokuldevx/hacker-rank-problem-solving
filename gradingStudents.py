import math

def gradingStudents(grades):
    # Write your code here
    con= []
    for i in range(len(grades)):
        round = math.ceil(grades[i]/5)*5                                     
        diff = round - grades[i]
        print(grades[i])
        if grades[i] < 3:
            con.append(grades[i])
        elif diff > 2:
            con.append(grades[i])
        else:
            con.append(round)
    return con


if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
