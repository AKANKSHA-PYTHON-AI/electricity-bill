print('=======XYZ SCHOOL=======')
print()
print('Details of 5 students.')
print()
details = {}
for i in range(5):
    roll_no = int(input('Enter student roll number : '))
    name = input('Enter name of the student : ').capitalize()
    marks = int(input('Enter student marks : '))
    grade = input("Enter the grade of the student : ").upper()
    print('Enter roll number of the student to get details of that student.')
    details[roll_no] = [name,marks,grade]
    print(details)


print('=========XYZ SCHOOL=========')
print()
print('displaying the details of the students.')
print()
def student_details():
    details = {}
    roll_num = int(input('enter th estudent roll number:'))
    name = input('enter name of the student:').strip().capitalize()
    marks = int(input('enter marks of the student:'))
    grade = input('enter grade of the sudent:').upper()
    details[roll_num] = [name,marks,grade]
    print(details)
    print(type(details))
student_details()
print(type(student_details))