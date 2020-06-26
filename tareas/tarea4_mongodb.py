from mongoengine import *

connect('padts')


# Esquema/Modelo
class estudiantes(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

    def saveE(name, email, password):
        for n, e, p in zip(name, email, password):
            students = estudiantes(name=n, email=e, password=p)
            students.save()

    def showE():
        for index, s in enumerate(estudiantes.objects):
            print('[{}] Nombre: {}\tEmail: {}\tPassword: {} '.format(
                index+1, s.name, s.email, s.password))

    def modifyE(temp, temp1):
        estudiantes.objects(name=temp).modify(name=temp1)

    def deleteE(name):
        estudiantes.objects(name=name).delete()

names = ['Juan', 'Blanca', 'Samantha', 'Felipe', 'Paulo']
emails = ['juan@gmail.com', 'blanca@email.com', 'sam@email.com', 'felp@gmail.com', 'paulo@gmail.com']
passwords = ['password1', 'password2', 'password3', 'password4', 'password5']

estudiantes.saveE(names, emails, passwords)
estudiantes.showE()
estudiantes.modifyE('Samantha', 'Juan')
estudiantes.deleteE('Paulo')
# test_delete = estudiantes.objects.first()
# test_delete.delete()
estudiantes.showE()

