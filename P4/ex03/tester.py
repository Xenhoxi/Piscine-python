from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)
print()

student = Student(name="Edward", surname="agle", id='noid')
try:
    print(student)
except Exception as err_msg:
    print(err_msg)
