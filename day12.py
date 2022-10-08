class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, t):
        super().__init__(firstName, lastName, idNumber)
        self.t = t
    def calculate(self):
        av=int(sum(self.t)/len(self.t))
        if 90 <= av <= 100:
            return 'O'
        elif 80 <= av < 90:
            return 'E'
        elif 70 <= av < 80:
            return 'A'
        elif 55 <= av < 70:
            return 'P'
        elif 40 <= av < 55:
            return 'D'
        else:
            return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())