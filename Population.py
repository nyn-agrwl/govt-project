import re
from fuzzywuzzy import process
import random

class Population:
	preposLoc="preposition.dat"
	city_regex="city_regex_new.txt"
	city_list="cities_list_new.txt"
	DNA=[]

	def __init__(self,input):
		self.input= input


	def removePreposition(self):
		self.input= " ".join([t for t in self.input.split() if t not in open(self.preposLoc).read().split('\n')])
		

	def fetch_cities(self): #UPDATE FOR THE NUMBERS
		self.city_dict={}
		file1= open(self.city_regex,"r").read().splitlines()
		file2= open(self.city_list,"r").read().splitlines()
		verify_cities= self.input.split()

		list_match=[]
		result=[]
		for verify_city in verify_cities:
			result.clear()
			length=len(verify_city)-2
			i=0
			for city in file1:
				
				if city[1]==chr(ord(verify_city[0]) + 1): #Evaluate the condition to increase speed in future
					if len(list_match)==0:
						break
					result=process.extract(verify_city,list_match,limit=3)
					recog_list=[]
				
					for recog_city in result:
						recog_list.append(recog_city[0])
					self.city_dict[verify_city]=recog_list
					break
				
				regex=city[0:(city.index('{')+1)]+str(length)+city[city.index('}'):len(city)]
				if re.match(regex,verify_city):
					list_match.append(file2[i])
				i=i+1
			list_match.clear()
		print(self.city_dict)
                

	def createTempPopulation(self):
		self.temp_population=[]
		for word in self.city_dict:
			self.temp_population.append(self.input.replace(" "+word,"")[0:])
		#print(self.temp_population)
	
	def setGenerator(self,stringLength,list0,sum=0): #improve
		temp=0
		randomNumber=random.randint( 1 , 5)
		if (randomNumber+sum)==stringLength:
			return randomNumber
		elif (randomNumber+sum)>stringLength:
			for i in range(1,randomNumber):
				if i+sum==stringLength:
					return i
		else:
			sum=sum+randomNumber
			list0.append(randomNumber)
			temp=self.setGenerator(stringLength,list0,sum)
			return temp
		list0.append(temp)


	def initializeDNA(self):
		randomSet=set()
		
		for i in range(1,20): #20 
			randomList=[]
			self.setGenerator(len(self.temp_population[0].split()),randomList)
			randomSet.add(tuple(randomList))
			1,5,1,4,
		

#house no5 road  bpl ,3
#split
#[house ,no5 ,road  ,bpl]
#join " " 3
#["house no5 road","bpl"]
#DNA(["house no5 road","bpl"])

		


obj =Population(" house no5  road  bpl") #temp.population=[house no5 road  bpl , house no5 hsbd road ]
obj.removePreposition() 					 #city_dict{hsbd:[hoshanknd],bpl:[bhopal,bopal,boduppal]}
obj.fetch_cities()							 #Population_list=[[["house no5","road bpl"],"house no5 road bpl","house no5 road,bpl","house,no5 road bpl"]]
obj.createTempPopulation()					 #Population_list=[[DNA1(["house no5","road bpl"]),[hoshangabad]),DNA2()]
obj.initializeDNA()						
