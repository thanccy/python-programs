def total_marks(marks):
    return sum(marks)
def average_marks(marks):
    return sum(marks)/len(marks)
def highest_marks(marks):
    return max(marks)
def lowest_marks(marks):
    return min(marks)
def grade_marks(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"

n=int(input("Enter number of students:"))
students=[]
for i in range(n):
    name=input("Enter student name:")
    marks=[]
    for j in range(3):
        mark=int(input("Enter mark:"))
        marks.append(mark)
    total=total_marks(marks)
    average=average_marks(marks)
    highest=highest_marks(marks)
    lowest=lowest_marks(marks)
    grade=grade_marks(average)
    students.append((name,total,average,highest,lowest,grade))
print("***students details**")
for student in students:
    print("name:",student[0])
    print("total:",student[1])
    print("average:",student[2])
    print("highest:",student[3])
    print("lowest:",student[4])
    print("grade:",student[5])
    print()
students.sort(key=lambda x: x[1])
print("sorted students based on their total:")
for student in students:
    print(student[1],"-",student[0])
    

