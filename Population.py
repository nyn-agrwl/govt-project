import re
from fuzzywuzzy import process
import random
import copy
from geopy.geocoders import Nominatim
from DNA import DNA
from SubPopulation import SubPopulation

class Population:
	preposLoc="preposition.dat"
	city_regex="city_regex_new.txt"
	city_list="cities_list_new.txt"
	Population=[]

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
	

	def setGenerator(self,stringLength,list0,sum=0): 
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
		
		TempPopulationList=[]
		self.PopulationList=[]

		for word in self.temp_population: 
			tempList=[]
			listofwords=word.split()
			for temp_set in randomSet:
				listOflocation=[] 
				start=0						#(2,1,) (2,) (3,) (1,) 
				location=""
				for number in temp_set: 
					for i in range(start,start+number):
						location+=(listofwords[i]+" ")
					listOflocation.append(location.strip())
					start=start+number
					location=""	
				for i in range(start,len(listofwords)):
					location+=(listofwords[i]+" ")
				listOflocation.append(location.strip())
				obj=DNA(listOflocation)
				tempList.append(obj)
			TempPopulationList.append(tempList) #2

		i=0
		for city in self.city_dict:
			for word in self.city_dict[city]:
				obj= SubPopulation(word,copy.deepcopy(TempPopulationList[i]))
				self.PopulationList.append(obj)
			i=i+1




	def placeLocator(self): #ISSUE HAI ABHI RUN MAT KARNA
		
		for member in self.PopulationList:
			city=member.getCity()
			DNAList=member.getDNAList()

		for member in self.PopulationList:
			city=member.getCity()
			DNAList=member.getDNAList()
			cache={}
			geolocator=Nominatim(user_agent="project",format_string="%s,"+city,timeout=10000)

			for DNAobj in DNAList:
				placeList=DNAobj.getNonRecognized()
				recognizedPlace=[]
				nonrecognizedPlace=[]
				for place in placeList:
					if place in cache:
						if cache[place]==1:
							recognizedPlace.append(place)
						else:
							nonrecognizedPlace.append(place)
					else :
						try:
							location= geolocator.geocode(place)
						except ValueError as error_message:
							print(error_message)
						if location is not None:
							print(place)
							print(location)
							cache[place]=1
							recognizedPlace.append(place)
						else:
							cache[place]=0
							nonrecognizedPlace.append(place)
				cache.clear()
				DNAobj.updateRecognizedWords(recognizedPlace)
				DNAobj.updateNonRecognizedWords(nonrecognizedPlace)

		print('RECOGNIZED_LISTS')		
		for member in self.PopulationList:
			DNAList=member.getDNAList()
			for DNAobj in DNAList:
				DNAobj.printRecognized()
		print('\n')
		print('NON_RECOGNIZED_LISTS')
		for member in self.PopulationList:
			DNAList=member.getDNAList()
			for DNAobj in DNAList:
				DNAobj.printNonRecognized()





	


obj =Population(" house no5 hoshangabad road  bpl")
obj.removePreposition()
obj.fetch_cities()					 
obj.createTempPopulation()
obj.initializeDNA()
obj.placeLocator()