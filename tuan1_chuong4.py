#------class-------
class student():
    name= ''
    age=0
    def __init__(self, name= '', age=0) :
        self.name=name
        self.age=age
    def show(self):
        print('My name is: ',self.name)
    def run(self):
        print('Student is running...')

class hai(student):
    def run(self):
        print ('Hai is running...')