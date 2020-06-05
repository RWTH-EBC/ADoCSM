import os
import numpy as np
from pathlib import Path
import linecache


class Class_Converter(object):
	######################################################################################################
	#Formats the file into a desired format
	def __init__(self,Aixlib_path):
		self.Aixlib_path =Aixlib_path
	
	## Read the modelica code and formats it to a better reading order. 
	#The parser will work with the newly formatted files later.
	def Model_Converter(self, filename_input, output_path, RelationModel, Aixlib_path): 
		Data = DataCheck(Aixlib_path)
		outputpath_temp = Data.set_temp_directory(output_path)
		self.RelationModel = RelationModel.split(".")
		self.RelationModel = self.RelationModel[len(self.RelationModel) - 1]
		RelationModel = self.RelationModel
		filename_output = Data.set_filename_output(filename_input, output_path, Aixlib_path, RelationModel)
	   
		readfile_in = open(filename_input, 'r')
		tempFilename_output = Data.set_tempFilename_output(output_path, filename_input, Aixlib_path, RelationModel)
		readfile_out = open(filename_output, "w")
		self.readfile_in = open(filename_input, "r")
		self.readfile_out = open(tempFilename_output, "w")
		count = 0
		counterlist = []
		for line in self.readfile_in.readlines():
			count = count +1
			line = line.lstrip()
			x = line.split()
			x_array = np.asarray(x)
			if line.find("/*")>-1:
				counterlist.append(count)
				continue
			if line.find("*/")>-1:
				counterlist.append(count)
				continue
			if len(line) > 1 and len(counterlist)%2==0:
				if line[0:2] != "//" :
					if line.find("=") > -1 :
						line = line.replace("=", " = ")
						self.readfile_out.write(line)
						continue
					if line.find("/*")>-1:
						continue
					if line.find("*/")>-1:
						continue
					if line.find("(") > -1 :
						line = line.replace("(", " ( ")
						self.readfile_out.write(line)
						continue
					if line.find(")") > -1 :
						line = line.replace(")", " ) ")
						self.readfile_out.write(line)
						continue
					if line.find(":") > -1:  #
						line = line.replace(";", " ; ")
						self.readfile_out.write(line)
						continue
					self.readfile_out.write(line)
		self.readfile_in.close()
		self.readfile_out.close()
		self.readfile_in = open(tempFilename_output, "r")
		self.readfile_out = open(filename_output, "w")
		content = self.readfile_in.read()
		content = content.split(';')
		array_Packager = []
		for i in range(0, len(content) - 1, 1):
			content[i] = content[i].replace("*/", "")
			content[i] = content[i].replace("\n", " ")
			content[i] = content[i].replace(";", " ; ")
			content[i] = content[i].replace("(", " ( ")
			content[i] = content[i].replace(")", " ) ")
			content[i] = content[i].lstrip()
			if content[i][0:2] == "/*":
				continue
			if content[i][0:7] == "package":
				array_Packager.append(1)
				array3 = []
				array31 = []
				for w in range(0, len(content[i]), 1):
					find0 = content[i][w].find('"')
					find1 = content[i][w].find(" ")
					if find0 > -1:
						array3.append(w)
					if find1 > -1:
						array31.append(w)
				if len(array3) > 1:		
					X = array3[1]
					Package = "\n" + content[i][0:X + 1] + "\n" + content[i][X + 1:]
					Package = Package.lstrip()
					self.readfile_out.write("\n" + Package)
				else:
					Y = array31[1]
					Package = "\n" + "\n" + content[i][0:Y + 1] + "\n" + content[i][Y + 1:] + "\n"
					Package = Package.lstrip()
					self.readfile_out.write("\n" + Package)
				continue
			if content[i][0:9] == "protected":
				protected = "\n" + content[i][0:9] + "\n" + content[i][10:] + "\n"
				self.readfile_out.write(protected)
				continue
			if content[i][0:16]=="initial equation":
				initialequation ="\n"+content[i][0:16] +"\n"+ content[i][17:]+"\n"
				self.readfile_out.write(initialequation)
				continue
			if content[i][0:8] == "equation":
				equation = "\n" + content[i][0:8] + "\n" + content[i][9:] + "\n"
				self.readfile_out.write(equation)
				continue
			if content[i][0:6] == "record":
				array1 = []
				for y in range(0, len(content[i])):
					find0 = content[i][y].find('"')
					if find0 > -1:
						array1.append(y)
				if len(array1)>1:
					stringModel = array1[1]  
					record = "\n" + content[i][0:stringModel+1] + "\n" + content[i][stringModel+2:] + "\n"
				else:
					T = (content[i].split())
					TList=""
					for w in T[2:]:
						TList=TList+" "+w
					TList=(TList.lstrip())
					record = "\n" + T[0] +" "+T[1]+" "+ "\n" + TList
				self.readfile_out.write(record)
				continue
			if content[i][0:8] == "function":
				array1 = []
				for y in range(0, len(content[i])):
					find0 = content[i][y].find('"')
					if find0 > -1:
						array1.append(y)
				if len(array1)>1:
					stringModel = array1[1]  
					functions = "\n" + content[i][0:stringModel+1] + "\n" + content[i][stringModel+2:] + "\n"
				else:
					T = (content[i].split())
					TList=""
					for w in T[2:]:
						TList=TList+" "+w
					TList=(TList.lstrip())
					functions = "\n" + T[0] +" "+T[1]+" "+ "\n" + TList
				self.readfile_out.write(functions)
				continue
			if content[i][0:5] == "block":
				array1 = []
				for y in range(0, len(content[i])):
					find0 = content[i][y].find('"')
					if find0 > -1:
						array1.append(y)
				if len(array1)>1:
					stringModel = array1[1]  
					block = "\n" + content[i][0:stringModel+1] + "\n" + content[i][stringModel+2:] + "\n"
				else:
					T = (content[i].split())
					TList=""
					for w in T[2:]:
						TList=TList+" "+w
					TList=(TList.lstrip())
					block = "\n" + T[0] +" "+T[1]+" "+ "\n" + TList
				self.readfile_out.write(block)
				continue
			if content[i][0:7] == "partial":
				array0 = []
				for w in range(0, len(content[i])):
					find0 = content[i][w].find('"')
					if find0 > -1:
						array0.append(w)
				if len(array0)>1:
					stringPartial = array0[1]  
					partial = "\n" + content[i][0:stringPartial + 1] + "\n" + content[i][stringPartial + 2:]
					self.readfile_out.write(partial)  
					continue
				else:
					T = (content[i].split())
					TList=""
					for w in T[3:]:
						TList=TList+" "+w
					TList=(TList.lstrip())
					partial = "\n" + T[0]+" "+T[1]+" "+T[2]+" "+"\n"+TList
					self.readfile_out.write(partial)  
					continue
			if content[i][0:5] == "model" :
				array1 = []
				for y in range(0, len(content[i])):
					find0 = content[i][y].find('"')
					if find0 > -1:
						array1.append(y)
				if len(array1)>1:
					stringModel = array1[1]		
					model = "\n" + content[i][0:stringModel + 1] + "\n" + content[i][stringModel + 2:].lstrip()
				else:
					T = (content[i].split())
					TList=""
					for w in T[2:]:
						TList=TList+" "+w
					model = "\n" + T[0] +" "+T[1]+" "+ "\n" + TList.lstrip()
				self.readfile_out.write(model)
				continue
			if content[i][0:9] == "connector":
				array2 = []
				for z in range(0, len(content[i])):
					find0 = content[i][z].find('"')
					if find0 > -1:
						array2.append(z)
				stringConnector = array2[1]
				connector = "\n" + content[i][0:stringConnector + 1] + "\n" + content[i][stringConnector + 2:]
				self.readfile_out.write(connector)   
				continue 
			self.readfile_out.write("\n" + content[i] + ";")
		self.readfile_in.close()
		self.readfile_out.close()
		
		###################################################################################################
		#If the file is a packages, the package searches for the searched model and stores it in a new file
		if len(array_Packager) > 0:
			readfile_in = open(filename_output, "r")
			T = filename_output.split("\\")
			T = T[len(T) - 1]		  
			T   = T[:-5]
			self.RelationModel = self.RelationModel.split()
			self.RelationModel = self.RelationModel[len(self.RelationModel)-1]
			self.RelationModel = self.RelationModel.replace(";","")
			file = outputpath_temp + "\\" + T + "." + self.RelationModel + ".java"
		  
			file= file.replace(".mo","")
			readfile_out = open(file, "w")
			array = []
			arraytype = []
			count = 0
			for line in readfile_in.readlines():
				count = count + 1
				x = line.split()
				x_array = np.asarray(x)
				if len(x_array) > 0:
					if len(x_array) > 1:
						if x_array[0] == "end" and x_array[1] == self.RelationModel + ";":
							
							array.append(count)
							pass
						if x_array[1] == self.RelationModel and x_array[0] !="input" and x_array[0] != "output":
						   
							array.append(count)
							pass
						if x_array[1] == self.RelationModel and x_array[0]=="type":
							
							arraytype.append(count)
							continue
							pass
						"""if  len(arraytype)==1 and x_array[0]=="annotation":
							print(line)
							arraytype.append(count)
							pass"""
						pass
					if len(x_array) > 2:
						if x_array[0] == "partial" and x_array[2] == self.RelationModel:
							array.append(count)
							pass
						pass
					pass
				continue
			pass
		
			if len(arraytype) > 1:
				for i in range(arraytype[0], arraytype[1] , 1):
					line = linecache.getline(filename_output, i)
					readfile_out.write(line)
					continue		
			elif len(arraytype) > 0:
				for i in range(arraytype[0], arraytype[0]+1 , 1):
					line = linecache.getline(filename_output, i)
					readfile_out.write(line)
					continue
		
			if len(array) > 1:
				for i in range(array[0], array[1] + 1, 1):
					line = linecache.getline(filename_output, i)
					readfile_out.write(line)
					continue
			elif len(array) > 0 :
				for i in range(array[0], array[0] + 1, 1):
					line = linecache.getline(filename_output, i)
					readfile_out.write(line)
					continue
				
			
			filename_output = file
		return filename_output 

## check paths and files for existence 	   
class DataCheck(object):
	def __init__(self,AixLib_path):
		self.AixLib_path = AixLib_path
		print("test")
	
	# Set folder directory in AixLib  
	def set_Folder_directory(self, AixLib_path):
		destination = AixLib_path
		suffixes = []
		for folder in os.listdir(AixLib_path):
			yield folder
	
	######################################################################################################
	#Search for the text file	 
	def set_relationmodel_path (self, AixLib_path, RelationModel, OriginalLibrary): 
		OriginalLibrary = OriginalLibrary.split(".")
		OriginalLibrary = OriginalLibrary[0].split("\\")
		ModelicaLibraries = DataCheck.allModelicaLibrary(self,AixLib_path)
		destination = AixLib_path
		RelationModel.split("=")
		if RelationModel.find("=") > -1:
			RelationModel = RelationModel[RelationModel.find("=") + 1:]
			RelationModel = RelationModel.replace(" ", "")
		RelationModel = RelationModel.split(".")
		RelationModel2=RelationModel[len(RelationModel)-1]
		RelationModel3 = RelationModel[:]
		suffixes = []
		for i in range(0, len(ModelicaLibraries), 1):
			if ModelicaLibraries[i] == RelationModel[0]:
				for x in range(1,len(RelationModel)-1):
					del RelationModel[len(RelationModel)-1]
					RelationModelStr=""
					for z in RelationModel:
						RelationModelStr = RelationModelStr+"\\"+z
						destination2= destination + "\\" 
						destination2 = destination+RelationModelStr
				   
					for root, dirs, files in os.walk(destination2):
						for w in range(len(RelationModel3)-1,0,-1):
							for file in Path(str(root)).iterdir():
								if file.suffix == '.mo' and file.stem == RelationModel3[w] :
									RelationModel_Path = root + '\\' + RelationModel3[w]+ file.suffix
									return RelationModel_Path 
								else:
									continue
					"""for root, dirs, files in os.walk(destination2):
						for file in Path(str(root)).iterdir():
							if file.suffix == '.mo' and file.stem == "package" :
									RelationModel_Path = root + '\\' + file.stem+ file.suffix
									return RelationModel_Path   """			
		OriginalLibraryList = "" 
		for w in OriginalLibrary[:len(OriginalLibrary)]:
			OriginalLibraryList = OriginalLibraryList + "\\" + w
		destination = (destination + OriginalLibraryList)
		for i in range(0, len(ModelicaLibraries), 1):
			if ModelicaLibraries[i] != RelationModel[0]:
				for root, dirs, files in os.walk(destination):
					for file in Path(str(root)).iterdir():
						for i in range(0, len(RelationModel), 1):
							if file.suffix == '.mo' and file.stem == RelationModel[len(RelationModel) - 1 - i] :
								RelationModel_Path = root + '\\' + RelationModel[len(RelationModel) - 1 - i] + file.suffix
								return RelationModel_Path 
							elif file.suffix == '.mo' and file.stem == OriginalLibrary[2]:
								RelationModel_Path = root + '\\' + OriginalLibrary[2] + file.suffix
								return RelationModel_Path
							else:
								continue
		destination = AixLib_path
		OriginalLibraryList = ""										 
		for w in OriginalLibrary[:len(OriginalLibrary)-1]:
			OriginalLibraryList = OriginalLibraryList + "\\" + w
		destination = (destination + OriginalLibraryList)
		for i in range(0, len(ModelicaLibraries), 1):
			if ModelicaLibraries[i] != RelationModel[0]:
				for root, dirs, files in os.walk(destination):
					for file in Path(str(root)).iterdir():
						for i in range(0, len(RelationModel), 1):
							if file.suffix == '.mo' and file.stem == RelationModel[len(RelationModel) - 1 - i] :
								RelationModel_Path = root + '\\' + RelationModel[len(RelationModel) - 1 - i] + file.suffix
								return RelationModel_Path 
							elif file.suffix == '.mo' and file.stem == OriginalLibrary[2]:
								RelationModel_Path = root + '\\' + OriginalLibrary[2] + file.suffix
								return RelationModel_Path
							else:
								break
		destination = AixLib_path
		
   
						 
	# set outputfile from inputfile   
	def setUMLModell(self, filename_input, output_path):
		readfile_in = open(filename_input, "r")
		filename_output = filename_input.split("\\")
		filename_output = filename_output[len(filename_output) - 1]
		filename_output = output_path + "\\" + filename_output
		return filename_output
	
	### Set the temporary file, where the formated text is located
	def set_temp_directory(self, output_path):
		outputpath_temp = output_path + "\\" + "TempData"
		if not os.path.exists(outputpath_temp):
			os.makedirs(outputpath_temp)
		return outputpath_temp   
	
	# Gives all libraries in the Library folder
	def allModelicaLibrary(self,Aixlib_path):
		#Aixlib_path = self.Aixlib_path
		self.Library = Aixlib_path
		self.ListLibrary = os.listdir(self.Library)
		return self.ListLibrary
   
	# Set temp outputfiles for formated text
	def set_tempFilename_output(self, output_path, filename_input, Aixlib_path, RelationModel):
		Library = DataCheck.allModelicaLibrary(self,Aixlib_path)
		filename_output = filename_input.split(".")
		filename_output = filename_output[0].split("\\")
		for i in range(0, len(Library), 1):
			for w in range(0, len(filename_output) - 1, 1):
				if filename_output[w] == Library[i]:
					filename_output = filename_output[w:]
					break
		StringList = ""  
		count = 0  
		for x in filename_output:
			count = count + 1
			if count == len(filename_output):
				StringList = StringList + str(x)
				break
			StringList = StringList + str(x) + "."
		T = StringList.split(".")
		T = T[len(T) - 1]
		tempFilename_output = output_path + "\\" + "tempdata\\" + StringList + ".txt"
		return tempFilename_output
	   
	def set_filename_output(self, filename_input, output_path, Aixlib_path, RelationModel): 
		Library = DataCheck.allModelicaLibrary(self,Aixlib_path)
		filename_output = filename_input.split(".")
		filename_output = filename_output[0].split("\\")
		for i in range(0, len(Library), 1):
			for w in range(0, len(filename_output) - 1, 1):
				if filename_output[w] == Library[i]:
					filename_output = filename_output[w:]
					break
		StringList = ""  
		count = 0  
		for x in filename_output:
			count = count + 1
			if count == len(filename_output):
				StringList = StringList + str(x)
				break
			StringList = StringList + str(x) + "."
		T = StringList.split(".")
		T = T[len(T) - 1]
		filename_output = output_path + "\\" + "tempdata\\" + StringList + ".java"
		return filename_output
	
	# Check whether the file exist
	def filename_exist(self, filename_input):
		try:
			with open(filename_input) as file:
				print("File exist!")
				file.close()
				pass
		except IOError:
			print ("Unable to open file \nFile don`t exist!") 
	
	# Check whether the aixlib path exist
	def AixLibPath_exist(self, AixLib_path):
		file_path = AixLib_path
		directory = os.path.dirname(file_path)
		try:
			os.stat(directory)
			print("AixLib directory exist!")
		except:
			print("Aixlib directory doesn`t exist!")
	
	# Append all translated models and used model in PlantUML Syntax in a single file
	def Appender(self, output_path, finalData):
		destination = output_path
		suffixes = []
		for path in Path(destination).iterdir():
			if path.is_file():
				suffixes.append(output_path + "\\" + path.stem + path.suffix)
		filename_input = open(finalData, "w")
		for i in range(0, len(suffixes)):
			input = open(suffixes[i], "r")
			for line in input:
				line = (line.replace("@startuml", ""))
				line = (line.replace("@enduml", ""))
				filename_input.write(line)
			input.close()  
		filename_input.close()
	
	# List models in a library package  
	def get_Modelsinpackages(self, filename_input , output_path):  
		readfile_in = open(filename_input, "r")
		RelationModel = []
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			if len(x_array) > 1 :
				if x_array[0] == "end" and x_array[1] != "if;":
					x_array[1]=x_array[1].replace(";","")
					RelationModel.append(filename_input[0:-5]+"."+x_array[1]+".java")
					continue
					pass
		readfile_in.close()
		return RelationModel
	# Translate models in library package
	def set_ModelsinPackages(self,filename_input , output_path): 
		readfile_in = open(filename_input, "r")
		counter = 0
		array = [] 
		array2 = []
		Model = DataCheck.get_Modelsinpackages(self,filename_input, output_path)
		ModelList = []
		filename_outputList = []
		for w in Model:
			ModelList.append(w)  
		if len(ModelList) >0:
			for line in readfile_in.readlines():
				x = line.split()
				x_array = np.asarray(x)
				counter = counter + 1
				if len(x_array) > 1 :
					for ModelPackage in ModelList:
						T = ModelPackage.split(".")
						if len(x_array)>2:
							if x_array[1] == T[-2] and x_array[0]!="package" and len(array)==0 :
								array.append(counter)
								Name = x_array[1] 
								continue
							if x_array[2] == T[-2] and x_array[0]!="package" and len(array2)==0 :
								array2.append(counter)
								Name2 = x_array[2] 
								continue
						if x_array[0] == "end" and x_array[1]==T[-2]+";":
							if len(array)>0 and Name== x_array[1].replace(";","") :
								array.append(counter)
								filename_output=ModelPackage
								readfile_out = open(filename_output, "w")
								filename_outputList.append(filename_output)
								for w in range(array[0],array[1]+1,1):
									line = linecache.getline(filename_input, w)
									readfile_out.write(line)
								array = []
								continue
							if len(array2)>0 and  Name2 == x_array[1].replace(";","") :
								
								array2.append(counter)
								filename_output=ModelPackage
								readfile_out = open(filename_output, "w")
								filename_outputList.append(filename_output)
								for w in range(array2[0],array2[1]+1,1):
									line = linecache.getline(filename_input, w)
									readfile_out.write(line)
								array2 = []
								continue
						if x_array[0] == "type" and x_array[1]==T[-2] :
							array.append(counter)
						if x_array[0] == "type" and len(array)==1 :
							array.append(counter)
							if len(array)>1:
								for w in range(array[0],array[1]+1,1):
									line = linecache.getline(filename_input, w)
									readfile_out.write(line)
									array = []
			return filename_outputList
			
	# List Packages in a library package
	def getPackagesinPackages(self,filename_input , output_path):
		readfile_in = open(filename_input, "r")
		counter = 0
		array = [] 
		array2 = []
		NameList = []
		filename_outputList = []
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			counter = counter + 1
			if len(x_array) > 1 :
				if x_array[0]=="package":
					NameList.append(filename_input[0:-5]+"."+x_array[1]+".java" )
					continue
		return NameList
	
	# Seperate a package in a package
	def getrowPackagesinPackages(self,filename_input , output_path):
		readfile_in = open(filename_input, "r")
		counter = 0
		array = [] 
		array2 = []
		NameList = []
		filename_outputList = []
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			counter = counter + 1
			if len(x_array) > 1 :
				if x_array[0]=="package":
					NameList.append((counter))
					continue
		return NameList
	  
	# Seperate a package in a package and write it as a single file
	def setPackagesinPackages(self,filename_input , output_path):
		readfile_in = open(filename_input, "r")
		NameList= DataCheck.getPackagesinPackages(filename_input , output_path)
		RowList = DataCheck.getrowPackagesinPackages(filename_input , output_path)
		array = []
		Path = filename_input.split(".")
		PackageList = []
		counter = 0
		if len(NameList)>0:
			for line in readfile_in.readlines():
				x = line.split()
				x_array =np.asarray(x)
				counter = counter +1 
				if len(x_array)>0:
					for Packages in NameList:
						T =Packages.split(".")
						if len(x_array)>1:
							if x_array[1].replace(";","")==T[-2] and x_array[0] =="end":
								array.append(counter)
								filename_output = Packages
								readfile_out = open(filename_output,"w")
								PackageList.append(filename_output)
								for w in range(RowList[0],array[0],1):
									line = linecache.getline(filename_input,w)
									readfile_out.write(line)
		 
	## Give the path of the model in a lower hierarchical level
	def showModel(self,ChildClass,RelationModel): 
		destination = ChildClass
		for root, dirs, files in os.walk(destination):
			for file in Path(str(root)).iterdir():
				if file.suffix == '.mo' and file.stem==RelationModel:
					RelationModel_Path = root + '\\' + file.stem+ file.suffix
					
					return RelationModel_Path
					continue
		
		
			


if __name__ == "__main__":   
	#DataCheck.set_ModelsinPackages(filename_input, output_path)
	from General import DataCheck
	DataCheck.showModel(ChildClass)