#3) Declare class --- college and initialize with required variables
 #Declare class ---Departments, Inherit college
 #Declare class Student inherit Department class
class Student :

    def setstudentid(self, id1):
        self.__studentid = id1

    def setqualifyingexammarks(self, marks):
        self.__qualifyingexammarks = marks

    def setdepartmentstatus(self, status):
        self.__departmentstatus = status

    def setyearofengg(self, year):
        self.__yearofengg = year

    def getstudentid(self):
        return self.__studentid

    def getqualifyingexammarks(self):
        return self.__qualifyingexammarks

    def getdepartmentstatus(self):
        return self.__departmentstatus

    def getyearofengg(self):
        return self.__yearofengg

objstu = Student()
objstu.setstudentid(1041)
objstu.setqualifyingexammarks(67.00)
objstu.setdepartmentstatus("CSE")
objstu.setyearofengg(2020)
print("Student Id : ", objstu.getstudentid())
print("Qualifying Exam Marks : ",objstu.getqualifyingexammarks())
print("Department Status : ",objstu.getdepartmentstatus())
print("Year of Engg. : ",objstu.getyearofengg())
