from DNA import DNA
class SubPopulation :
	
	def __init__(self,city,memberList):
		self.city=city
		self.memberList=memberList

	def getDNAList(self):
		return self.memberList

	def getCity(self):
		return self.city

	def printDNAListNon(self):
		for DNAobj in self.memberList:
			DNAobj.printNonRecognized()

