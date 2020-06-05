
import os
import shutil
import numpy as np
import re

#ClassConverter = General.Class_Converter()
#Realtion =  Object_Oriented_Relations.Relation()

#DataCheck = General.DataCheck
#ClassDiagram = ClassDiagram.ClassDiagram()

class UMLClassDiagram_MainInterface(object):
	
	def __init__(self, AixLib_path):
		self.AixLib_path = AixLib_path
	
	### Class interface: Search for relations, parameters and used classes and translate in plantuml syntax
	def Class_Interface(self,filename_input,output_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,relations,showconstant,showType):
		AixLib_path= self.AixLib_path
		# Import Libraries
		from General import DataCheck
		from General import Class_Converter
		from Object_Oriented_Relations import Relation
		from ClassDiagram import ClassDiagram
		##Deletes the files in the OutputPath
		ClassConverter = Class_Converter(self.AixLib_path)
		fileList = os.listdir(output_path)
		
		for f in fileList:
			f=output_path+"\\"+f
			if os.path.isfile(f):
				os.remove(f)
		
		## Checks if path and file are correct
		DataCheck.AixLibPath_exist(self,self.AixLib_path) #Check if the directory exists with Modelica libraries
		DataCheck.filename_exist(self,filename_input) #Check if the file exists
		Model1 = []
		Model11 = []
		Model2 = []
		Model21 = []
		Model3 = []
		Model31 = []
		Model4 = []
		Model41 = []
		Model5 = []
		Model51 = []
		Model6 = []
		Model61 = []
		Model7 = []
		Model71 = []
		Model8 = []
		Model81 = []
		Model9 = []
		Model91 = []
		Model10 = []
		Model11 = []
		Package = []
		
		RelationModel = filename_input.split(".")
		RelationModel = RelationModel[0].split("\\")
		RelationModel = RelationModel[len(RelationModel)-1]
		Relations = Relation(self.AixLib_path)
		##Hierarchy Level 1
		###############################################################################################################################################################################################
		if HierarchyLevel > 0 :
			filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file
			##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
			ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,relations,showconstant,showType)
			DataCheck.filename_exist(self,filename_input) #Check if the file exists
			for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
				ClassDiagram.insert_line(self,filename_input,output_path,ClassDiagram.number_of_lines(self,filename_input,output_path)-1,"\n"+z+"\n" )
				continue
		
		##Hierarchy Level 2
		###############################################################################################################################################################################################
		if HierarchyLevel > 1:
			for i in Relations.get_Relation(filename_input,self.AixLib_path,block): #Find the relations from the child class
				i= i.split(",")
				filename_input = i[0] 
				RelationModel = i[1]
				filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file
				DataCheck.filename_exist(self,filename_input) #Check if the file exists
				
				##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
				ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
				Model1.append(filename_input)
				for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
					ClassDiagram.insert_line(self,filename_input,output_path,ClassDiagram.number_of_lines(self,filename_input,output_path)-1,"\n"+z+"\n" )
					continue
		
		##Hierarchy Level 3
		###############################################################################################################################################################################################
		if HierarchyLevel >2 :
			for w in range(0,len(Model1),1):
				for i in Relations.get_Relation(Model1[w],AixLib_path,block): #Find the relations from the child class
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file 
					
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
					   
						Model2.append(T[i])
						Model21.append(T[i])
					Model2.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,filename_input,output_path, ClassDiagram.number_of_lines(self,filename_input,output_path)-1,"\n"+z+"\n" )
			for x in range(0,len(Model21),1):
					for z in Relations.set_relation(Model21[x], AixLib_path): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,Model21[x],output_path, ClassDiagram.number_of_lines(self,Model21[x],output_path)-1,"\n"+z +"\n")
	   
		##Hierarchy Level 4
		###############################################################################################################################################################################################
		if HierarchyLevel >3:
			for w in range(0,len(Model2),1):
				for i in Relations.get_Relation(Model2[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
					  
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file  
				   
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						
						Model31.append(T[i])
						Model3.append(T[i])
						continue
					Model3.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,filename_input,output_path, ClassDiagram.number_of_lines(self,filename_input,output_path)-1,"\n"+z +"\n")
						continue
				for x in range(0,len(Model31),1):
					for z in Relations.set_relation(Model31[x]): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,Model31[x],output_path, ClassDiagram.number_of_lines(self,Model31[x],output_path)-1,"\n"+z +"\n")
		
		##Hierarchy Level 5
		###############################################################################################################################################################################################
		if HierarchyLevel >4 :
			for w in range(0,len(Model3),1):
				for i in Relations.get_Relation(Model3[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
				  
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file 
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					#print(Package)
					Package = []
					for i in range(0,len(T),1):
						Model41.append(T[i])
						Model4.append(T[i])
						continue
					Model4.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,filename_input,output_path, ClassDiagram.number_of_lines(self,filename_input,output_path)-1,"\n"+z +"\n")
						continue
				for x in range(0,len(Model41),1):
					for z in Relations.set_relation(Model41[x]): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(Model41[x],output_path, ClassDiagram.number_of_lines(Model41[x],output_path)-1,"\n"+z +"\n")
		
		##Hierarchy Level 6
		###############################################################################################################################################################################################
		if HierarchyLevel >5 :
			for w in range(0,len(Model4),1):
				for i in Relations.get_Relation(Model4[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)  #Formats the file and outputs the file
				   
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						Model51.append(T[i])
						Model5.append(T[i])
						continue
					Model5.append(filename_input)
					for z in Relations.set_relation(filename_input ): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,filename_input,output_path, ClassDiagram.number_of_lines(self,filename_input,output_path)-1,"\n"+z +"\n")
			for x in range(0,len(Model51),1):
					for z in Relations.set_relation(Model51[x] ): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,Model51[x],output_path, ClassDiagram.number_of_lines(self,Model51[x],output_path)-1,"\n"+z +"\n")
		##Hierarchy Level 7
		###############################################################################################################################################################################################
		if HierarchyLevel >6 :
			for w in range(0,len(Model5),1):
				for i in Relations.get_Relation(Model5[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)  #Formats the file and outputs the file
				   ##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						Model61.append(T[i])
						Model6.append(T[i])
						continue
					
					Model6.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,filename_input,output_path, 1,"\n"+z +"\n")
				for x in range(0,len(Model61),1):
					for z in Relations.set_relation(Model61[x]): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(self,Model61[x],output_path, ClassDiagram.number_of_lines(Model61[x],output_path)-1,"\n"+z +"\n")
		
		##Hierarchy Level 8
		###############################################################################################################################################################################################
		if HierarchyLevel >7 :
			for w in range(0,len(Model6),1):
				for i in Relations.get_Relation(Model6[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					   
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file 
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						Model71.append(T[i])
						Model7.append(T[i])
						continue
					Model7.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
				for x in range(0,len(Model71),1):
					for z in Relations.set_relation(Model71[x]): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(Model71[x],output_path, ClassDiagram.number_of_lines(Model71[x],output_path)-1,"\n"+z +"\n")
		
		##Hierarchy Level 9
		###############################################################################################################################################################################################
		if HierarchyLevel >8 :
			for w in range(0,len(Model7),1):
				for i in Relations.get_Relation(Model7[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file 
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						Model81.append(T[i])
						Model8.append(T[i])
						continue
					Model8.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
			for x in range(0,len(Model81),1): 
					for z in Relations.set_relation(Model81[x]): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(Model81[x],output_path, ClassDiagram.number_of_lines(Model81[x],output_path)-1,"\n"+z +"\n")
		
		##Hierarchy Level 10
		###############################################################################################################################################################################################
		if HierarchyLevel >9 :
			for w in range(0,len( Model8),1):
				for i in Relations.get_Relation(Model8[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1]
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)  #Formats the file and outputs the file
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						Model91.append(T[i])
						Model9.append(T[i])
						continue
					Model9.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
		for x in range(0,len(Model91),1):
					for z in Relations.set_relation(Model91[x]): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(Model91[x],output_path, ClassDiagram.number_of_lines(Model91[x],output_path)-1,"\n"+z +"\n")
		
		##Hierarchy Level 11
		###############################################################################################################################################################################################
		if HierarchyLevel >10 :
			for w in range(0,len(Model9),1):
				for i in Relations.get_Relation(Model9[w],AixLib_path,block): #Find the relations from the child class
					Package = []
					i= i.split(",")
					if len(i)==3:
						filename_input = i[0] 
						RelationModel = i[1]
						Package.append(i[2])
					else:
						filename_input = i[0] 
						RelationModel = i[1] 
					DataCheck.filename_exist(self,filename_input) #Check if the file exists
					filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file 
					##Sets the class with parameters, variables, methods, .., in PlantUML Syntax
					T = ClassDiagram.put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
					Package = []
					for i in range(0,len(T),1):
						Model10.append(T[i])
						Model11.append(T[i])
						continue
					Model10.append(filename_input)
					for z in Relations.set_relation(filename_input): #Adds the relations in PlantUMl format to the text file
						ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
			for x in range(0,len(Model11),1):
				for z in Relations.set_relation(Model11[x]): #Adds the relations in PlantUMl format to the text file
					ClassDiagram.insert_line(Model11[x],output_path, ClassDiagram.number_of_lines(Model11[x],output_path)-1,"\n"+z +"\n")
	
	## Write at the beginning and end of the PlantUML Code arguments
	def start_end_syntax(self,filename_output,insert_pos,line):
		f = open(filename_output,"r+")
		lines = f.readlines()
		f.close()
		lines.insert(insert_pos, line)
		f = open(filename_output, 'w')
		f.writelines(lines)
		f.close()
	
	def test2(self,finalData):
		file = open(finalData,"r")
		lines = file.readlines()
		numberLines =  len(lines)
		return numberLines
		file.close()
	
	#Sorts the file by classes and relations
	###############################################################################################################################################################################################
	def sort(self,finalData,finalData2): 
		readfile_in = open(finalData,"r")
		readfile_out = open(finalData2,"w")
		RelationList = []
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			#if x_array[0]=="package":
			#	x_array[1]=
				
			if line.find("<|--")>-1 or line.find("--*")>-1 or line.find("<|..")>-1 or line.find("@enduml")>-1:
				RelationList.append(line)#
			else:
				readfile_out.writelines(line)
		for w in RelationList:
			readfile_out.writelines("\n"+w+"\n")
			
	## delete enum in files 	
	def delelteTypeRelation(self,finalData):
		EnumList = []
		CounterList = []
		readfile_in = open(finalData,"r+")
		count = 0
		for line in readfile_in.readlines():
			count = count +1
			x = line.split()
			x_array = np.asarray(x)
			if len(x_array) > 0:
				if x_array[0] =="enum":
					EnumList.append(x_array[1])
					continue
				for w in EnumList:
					if w == x_array[len(x_array)-1]:
						readfile_in.truncate()
						del line[0]
						CounterList.append(count)
						continue
						
					
		
	
			

if __name__ == "__main__":
	### Import Libraries
	from General import *
	from Object_Oriented_Relations import Relation
	from ClassDiagram import ClassDiagram
	
	## Configure Files
	filename_input=r"D:\Gitlab\Bachelorarbeit\Library\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves\IsenthalpicExpansionValve.mo"
	AixLib_path=r"D:\Gitlab\Bachelorarbeit\Library"
	output_path =  r"D:\Gitlab\Bachelorarbeit\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
	Model = [filename_input]
	finalData = r"D:\Gitlab\Bachelorarbeit\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil.java"
	finalData2 = r"D:\Gitlab\Bachelorarbeit\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil2.java"
		
	# Configure Parameters
	parameter = True
	variables = False
	relations = False
	Medium = False
	primitivevariables = False
	methode = False
	complexvariables = False 
	HierarchyLevel = 6
	block = False
	showPackages = True 
	showconstant = False
	showType = False
	
	print("start")	
	Data = DataCheck(AixLib_path)
 
	# Start the Parser functions
	Instanz = UMLClassDiagram_MainInterface(AixLib_path)
	Instanz.Class_Interface(filename_input, output_path, HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,relations,showconstant,showType)  
	# Append all translated models and used model in PlantUML Syntax in a single file
	Data.Appender(output_path, finalData)
	## Add startuml und enduml in plantuml file
	Instanz.start_end_syntax(finalData,0,"@startuml{")	
	Instanz.start_end_syntax(finalData,Instanz.test2(finalData), " \n @enduml")  
	Instanz.sort(finalData,finalData2)
	
	print("Conversion Erfolgreich!")
	
	#Instanz.delelteTypeRelation(r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil2.java")
	#t= output_path+"\\"+"TempData"
	#shutil.rmtree(t)
	
	 
	 
 
 
 
	
	

