
class DNA:
	nonRecognized=[]
	recognized=[]
	fitness=0

#[5:57 PM, 3/31/2020] Nayan SIRT: update wordlist()
#[5:57 PM, 3/31/2020] Nayan SIRT: updaterecognized word list()
#[5:57 PM, 3/31/2020] Nayan SIRT: fitness score data member=0
#[5:58 PM, 3/31/2020] Nayan SIRT: CalculatFitnesScore()
#[5:58 PM, 3/31/2020] Nayan SIRT: static function normalize(DNA[])

	def __init__(self,nonRecognized):
		self.nonRecognized=nonRecognized

	def updateNonRecogWords(self,nonRecognized):
		self.nonRecognized=nonRecognized

	def updateRecognizedWords(self,recognized):
		self.recognized=recognized

	def calculateFitnessScore(self):
		for words in self.recognized:
			self.fitness+=len(words.split())

	def printFitnessScore(self):
		print(self.fitness)




