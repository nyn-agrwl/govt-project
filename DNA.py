
class DNA:
	nonRecognized=[] #nonRecognized=["house no5","road bpl"]
	recognized=[]
	fitness=0 

	def __init__(self,nonRecognized):
		self.nonRecognized=nonRecognized

	def getNonRecognized(self):
		return self.nonRecognized

	def getRecognized(self):
		return self.recognized

	def updateNonRecognizedWords(self,nonRecognized):
		self.nonRecognized=nonRecognized

	def updateRecognizedWords(self,recognized):
		self.recognized=recognized

	def calculateFitnessScore(self):
		for words in self.recognized:
			self.fitness+=len(words.split())

	def printFitnessScore(self):
		print(self.fitness)

	def printNonRecognized(self):
		print(self.nonRecognized)

	def printRecognized(self):
		print(self.recognized)




