import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Population:
	preposLoc="preposition.dat"
	city_regex="city_regex_new.txt"
	city_list="cities_list_new.txt"

	def __init__(self,input):
		self.input= input


	def removePreposition(self):
		self.input= " ".join([t for t in self.input.split() if t not in open(self.preposLoc).read().split('\n')])


	def printInput(self):
		print(self.input)
		

	def fetch_cities(self):
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
		print(self.temp_population)

obj =Population(" house no.5 near hoshbd road bpl")
obj.printInput()
obj.removePreposition()
obj.fetch_cities()
obj.printInput()
obj.createTempPopulation()