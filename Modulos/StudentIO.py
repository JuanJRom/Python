import shelve

try:
    import cPickle as pickle
except ImportError:
    import pickle


class student():
    __name = ''
    __email = ''
    __password = ''

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def saveStudentP(students):
        file = open('studentsP.db', 'wb')
        pickle.dump(students, file)
        file.close()

    def readStudentP(file_name):
        file = open(file_name, 'rb')
        unpickler = pickle.Unpickler(file)
        read_students = unpickler.load()
        file.close()
        return read_students

    def saveStudentS(n, e, p):
        with shelve.open('studentsS.db') as shelf:
            for i, j, k in zip(n, e, p):
                temp = student(i, j, k)
                shelf[i] = temp

    def readStudentS():
        with shelve.open('studentsS.db') as shelf:
            temp = []
            for key in shelf.keys():
                temp.append(shelf[key])
            return temp

    def __str__(self):
        string = 'Name: {}\nEmail: {}\nPassword: {}'.format(self.getName(), self.getEmail(), self.getPassword())
        return string