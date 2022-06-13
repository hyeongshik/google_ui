class StudentClass :
   def __init__(self, age, name):
       self.age = age
       self.name = name
    def showName(self):

Class  Parent :
    def work(self) :
        print("일을 한다")

Class Child(Parent) :
    def play(self) :
        print("놀기")

worker1 = Parent()
worker1.work()

child1 = Child()
child1.play()
child1.work()

stu1 = StudentClass(10,"홍길동")
stu1 = StudentClass(59,"김형식")

stu1.name
stu1.showName()



