# Homework 3
from Modulos import StudentIO

names = ['Juan', 'Blanca', 'Samantha', 'Felipe', 'Paulo']
emails = ['juan@gmail.com', 'blanca@email.com', 'sam@email.com', 'felp@gmail.com', 'paulo@gmail.com']
passwords = ['password1', 'password2', 'password3', 'password4', 'password5']

students = []
for n, e, p in zip(names, emails, passwords):
    students.append(StudentIO.student(n, e, p))

StudentIO.student.saveStudentP(students)
print('\nObjects read with pickle\n')
r = StudentIO.student.readStudentP('studentsP.db')
for i in r:
    print(i)
StudentIO.student.saveStudentS(names, emails, passwords)
print('\nObjects read with shelve\n')
r2 = StudentIO.student.readStudentS()
for i in r2:
    print(i)
# No se si entendi mal esta parte, pero creo que si utilizamos el método de "save"
# sobreescribe el archivo y asi seria como actualizar los datos 
