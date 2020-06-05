import numpy as np
from General import *
from ClassDiagram import *
import os

#DataCheck = General.DataCheck
#ClassDiagram = ClassDiagram.ClassDiagram()


class Relation(object):
	
	def __init__(self,AixLib_path):
		self.AixLib_path = AixLib_path
		
	## Translate relation for classes, used classes, imports in PlantUML Syntax
	def set_relation(self, filename_input):
		Data = DataCheck(self.AixLib_path)
		self.ListLibrary = Data.allModelicaLibrary(self.AixLib_path)
		self.filename_input = filename_input
		readfile_in = open(self.filename_input, 'r+')
		array0 = []
		array1 = []
		array2 = []
		x_modelica = []
		mainModel = filename_input
		mainModel = mainModel.split("\\")
		mainModel = mainModel[len(mainModel) - 1].split(".")
		mainModel = mainModel[len(mainModel) - 2]
		for line in readfile_in.readlines():
			x = line.split()
			y = line.split(".")
			x_array = np.asarray(x)
			if len(x_array) > 0:
				# Loop break if equation, annotationor algorithm part is reached
				if x_array[0] =="equation" or x_array[0] =="annotation" or x_array[0] =="algorithm":
					break
				# Used classes declared as parameter or final
				if len(x_array)>1:
					x_modelica = x_array[1].split(".")
					if len(x_modelica)>2:
						if x_array[0] == "parameter"  and x_modelica[1]!="SIunits"  and x_modelica[0]!="Medium":
							y = line.find('"')
							Model2 = x_array[2]
							Model = x_array[1].split(".")
							Model[len(Model)-1].replace("]","")
							relation = Model[len(Model)-1] + " -down--* " + '"' + Model2 + '"' + mainModel
							yield relation
							continue
						elif x_array[0] == "final"  and x_modelica[1]!="SIunits"  and x_modelica[0]!="Medium":
							y = line.find('"')
							Model2 = x_array[2]
							Model = x_array[1].split(".")
							Model[len(Model)-1].replace("]","")
							relation = Model[len(Model)-1] + " -down--* " + '"' + Model2 + '"' + mainModel
							yield relation
							continue
				# Import Models
				if x_array[0] == "import":
					array2.append(x_array)
					y = array2[0][1].split('.')
					y = np.asarray(y)
					RelationModel = (array2[0][1])
					RelationModel = RelationModel.lstrip()
					ExtendedModel = x_array[len(x_array) - 1].replace(";","")
					ExtendedModel = ExtendedModel.split(".")
					ExtendedModel = ExtendedModel[len(ExtendedModel)-1]
					relation = ExtendedModel + " <..-down " + '"' + "<<import>>" + '"' + mainModel
					yield relation
				# Relation part	
				if x_array[0] == "extends":
					array0.append(x_array)
					y = array0[0][1].split('.')
					y = np.asarray(y)
					ExtendedModel = (x_array[1].split("."))
					ExtendedModel = ExtendedModel[len(ExtendedModel)-1]
					if ExtendedModel.find("(")>-1:
						ExtendedModel = ExtendedModel[:ExtendedModel.find("(")-1]
					ExtendedModel = ExtendedModel.replace(";","")
					relation = ExtendedModel + " <|---up " + mainModel
					yield relation
					continue
					pass
				if x_array[0]=="outer":
					Model = x_array[2]
					ExtendedModel = x_array[1] 
					relation = ExtendedModel+" o---up " + '"' + Model + '"' +mainModel
					yield relation
					continue
					pass
				
				if x_array[0]=="inner":
					Model = x_array[2]
					ExtendedModel = x_array[1] 
					ExtendedModel.replace("]","")
				   
					relation = ExtendedModel+" *---up " + '"' + Model + '"' +mainModel
					yield relation
					continue
					pass
				 
				# if x_array0] == "connect":
				 #   array0.append(x_array)
				  #  model1 = line[line.find("(")+2:line.find(",")]
				   # model2 =line [line.find(",")+1:line.find(")")]
					# str = model1  +" #.. "+ model2
				  
					# relation = str
					# yield relation 
					# pass   
				if x_array[0] == "replaceable" and x_array[1] == "model":
					FirstModel = (line[line.find("=") + 1:line.find("constrainedby") - 1])
					Model = x_array[2]
					FirstModel = FirstModel.lstrip()
					RelationModel = FirstModel
					FirstModel = FirstModel.split(".")
					FirstModel = FirstModel[len(FirstModel) - 1]
					SecondModel = (line[line.find("constrainedby") + 13:line.find('"') - 1])
					RelationModel = SecondModel.lstrip()
					SecondModel = SecondModel.lstrip()
					SecondModel = SecondModel.split(".")
					SecondModel = SecondModel[len(SecondModel) - 1]
					array1.append(x_array)
					y = array1[0][1].split('.')
					y = np.asarray(y)
					PolymorphismModel = y[len(y) - 1].split(';')
					PolymorphismModel = PolymorphismModel[0].split("(") 
					PolymorphismModel = PolymorphismModel[0]
					relation = FirstModel + " <|..-up " + '"' + Model + '"' + mainModel
					yield relation
					pass
				
				if x_array[0] == "replaceable" and x_array[1] == "package":
					if line.find("constrainedby") > -1:
						FirstModel = (line[line.find("=") + 1:line.find("constrainedby") - 1])
					else:	
						FirstModel = (line[line.find("=") + 1:line.find('"') - 1])
				   
					FirstModel = FirstModel.lstrip()
					Model = x_array[2]
					RelationModel = FirstModel
					SecondModel = (line[line.find("constrainedby") + 13:line.find('"') - 1])
					RelationModel = SecondModel.lstrip()
					SecondModel = SecondModel.lstrip()
					SecondModel = SecondModel.split(".")
					SecondModel = SecondModel[len(SecondModel) - 1]
					array1.append(x_array)
					y = array1[0][1].split('.')
					y = np.asarray(y)
					PolymorphismModel = y[len(y) - 1].split(';')
					PolymorphismModel = PolymorphismModel[0].split("(") 
					PolymorphismModel = PolymorphismModel[0]
					relation = FirstModel + " <|..-up " + '"' + Model + '"' + mainModel
					yield relation
					pass
				
				if x_array[0] == "replaceable" and x_array[1] != "package" and x_array[1] != "model":
					Model = x_array[2]
					FirstModel = x_array[1].split(".")
					FirstModel = FirstModel[len(FirstModel)-1]
					FirstModel = FirstModel.lstrip()
					RelationModel = FirstModel
					SecondModel = (line[line.find("constrainedby") + 13:line.find('"') - 1])
					RelationModel = SecondModel.lstrip()
					SecondModel = SecondModel.lstrip()
					SecondModel = SecondModel.split(".")
					SecondModel = SecondModel[len(SecondModel) - 1]
					array1.append(x_array)
					y = array1[0][1].split('.')
					y = np.asarray(y)
					PolymorphismModel = y[len(y) - 1].split(';')
					PolymorphismModel = PolymorphismModel[0].split("(") 
					PolymorphismModel = PolymorphismModel[0]
					relation = FirstModel + " <|..-up " + '"' + Model + '"' + mainModel
					yield relation
					pass
				count = 0
				for i in range(0, len(self.ListLibrary), 1):
					count = count +1
					Libraries = x_array[0].split(".")
					Libraries = Libraries[0]
					FirstArray = x_array[0].split(".")
					if Libraries == self.ListLibrary[i] and x_array[0][9:16] != "SIunits": 
						Model = x_array[0].split(".")
						Model2 = x_array[1].split("(")
						Model = (Model[len(Model) - 1])
						Model = Model.replace("]","")
						if len(Model2)>0 and Model2[0]!="":
							relation = Model + " -down--* " + '"' + Model2[0] + '"' + mainModel
						else:
							relation = Model + " -down--* " +  mainModel
						yield relation
						continue
						pass
					
					elif count<len(self.ListLibrary):
						continue
					
					elif Libraries != self.ListLibrary[i] and FirstArray[0] != "Medium":
						T = filename_input.split("\\")
						T = (T[len(T)-1])
						T = T.split(".")
						x_Modelica = x_array[0].split(".")
						AixLib_path2 =self.AixLib_path+"\\"+T[0]+"\\"+T[1]
						Model = x_Modelica[len(x_Modelica)-1]
						if x_Modelica[0] !="Modelica":
							X = Data.showModel(AixLib_path2,Model)
							if X != None:
								X = X.split("\\")
								X = X[len(X)-1].replace(".mo","")
								relation = Model + " -down--* "  + '"' + x_array[1].replace("(","") + '"'+  mainModel
								yield relation
							else:
								continue
					
	## Search for classes with relation for classes, used classes, imports in PlantUML Syntax	
	def get_Relation(self, filename_input, AixLib_path,block):
		Data = DataCheck(self.AixLib_path)
		self.ListLibrary = Data.allModelicaLibrary(AixLib_path)
		self.filename_input = filename_input
		readfile_in = open(self.filename_input, 'r+')
		array0 = []
		array1 = []
		array2 = []
		array3 = []
		mainModel = filename_input
		mainModel = mainModel.split("\\")
		mainModel = mainModel[len(mainModel) - 1].split(".")
		OriginalLibrary = ""
		count = 0
		for w in mainModel[0:3]:
			count = count + 1 
			if count == 3:
				OriginalLibrary = OriginalLibrary + w
			else:
				OriginalLibrary = OriginalLibrary + w + "\\"
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			if len(x_array) > 1:
				x_modelica = x_array[1].split(".")
			if len(x_array) > 0:
				if x_array[0] =="equation" or x_array[0] =="annotation" or x_array[0] =="algorithm":
					break
				if block == False:
					test = x_array[0].split(".")
					if test[0] == "Modelica" and test[1] =="Blocks"  :
						continue
				if x_array[0] == "import":
					array2.append(x_array)
					if line.find("=")>-1:
						RelationModel = x_array[3].replace(";","")
						relation_directory = DataCheck.set_relationmodel_path(AixLib_path, RelationModel, OriginalLibrary)
					else:
						RelationModel = (array2[0][1])
						RelationModel = RelationModel.lstrip()
						RelationModel = RelationModel.replace(";", "")
						relation_directory = DataCheck.set_relationmodel_path(AixLib_path, RelationModel, OriginalLibrary)
					if relation_directory!=None:
						Package = RelationModel
						#print(relation_directory + "," + RelationModel+","+Package)
						#yield relation_directory + "," + RelationModel+","+Package
						#yield relation_directory + "," + RelationModel
					else:
						continue
				
				if x_array[0] == "extends":
					array0.append(x_array)
					y = array0[0][1].split('.')
					y = np.asarray(y)
					RelationModel=x_array[1]
					relation_directory = Data.set_relationmodel_path(AixLib_path, RelationModel, OriginalLibrary)
					if relation_directory == None:
						continue
					yield relation_directory + "," + RelationModel
				
				
				if x_array[0] == "inner":
					array0.append(x_array)
					y = array0[0][1].split('.')
					y = np.asarray(y)
					RelationModel = (array0[0][1])
					RelationModel = RelationModel.lstrip()
					RelationModel = RelationModel.replace(";", "")
					relation_directory = DataCheck.set_relationmodel_path(AixLib_path, RelationModel, OriginalLibrary)
					if relation_directory == None:
						continue
					yield relation_directory + "," + RelationModel
				
				if x_array[0] == "outer":
					array0.append(x_array)
					y = array0[0][1].split('.')
					y = np.asarray(y)
					RelationModel = (array0[0][1])
					RelationModel = RelationModel.lstrip()
					RelationModel = RelationModel.replace(";", "")
					relation_directory = DataCheck.set_relationmodel_path(AixLib_path, RelationModel, OriginalLibrary)
					if relation_directory == None:
						continue
					yield relation_directory + "," + RelationModel 
				# if x_array[0] == "connect":
				 #   array0.append(x_array)
				  #   
				   # model1 = line[line.find("(")+2:line.find(",")]
				   # model2 =line [line.find(",")+1:line.find(")")]
					# str = model1  +" #.. "+ model2
				  
					# relation = str
					# yield relation	
				if len(x_array)>1:
					if x_array[0] == "replaceable" and x_array[1] == "model":
						FirstModel = (line[line.find("=") + 1:line.find("constrainedby") - 1])
						FirstModel = FirstModel.lstrip()
						Package = (FirstModel)
						
						RelationModel = FirstModel
						FirstModel = FirstModel.split(".")
						FirstModel = FirstModel[len(FirstModel) - 1]
						SecondModel = (line[line.find("constrainedby") + 13:line.find('"') - 1])
						relation_directory = DataCheck.set_relationmodel_path(self,AixLib_path, RelationModel, OriginalLibrary)
						SecondModel = SecondModel.lstrip()
						SecondModel = SecondModel.split(".")
						SecondModel = SecondModel[len(SecondModel) - 1]
						array1.append(x_array)
						y = array1[0][1].split('.')
						y = np.asarray(y)
						PolymorphismModel = y[len(y) - 1].split(';')
						PolymorphismModel = PolymorphismModel[0].split("(") 
						PolymorphismModel = PolymorphismModel[0]
						if relation_directory == None:
							continue
				  
						yield relation_directory + "," + RelationModel+","+Package
			
				if x_array[0] == "replaceable" and x_array[1] == "package":
					if line.find("constrainedby") > -1:
						FirstModel = (line[line.find("=") + 1:line.find("constrainedby") - 1])
					else:	
						FirstModel = (line[line.find("=") + 1:line.find('"') - 1])
					FirstModel = FirstModel.lstrip()
					Package = (FirstModel)
					RelationModel = FirstModel
					FirstModel = FirstModel.split(".")
					FirstModel = FirstModel[len(FirstModel) - 1]
					SecondModel = (line[line.find("constrainedby") + 13:line.find('"') - 1])
					RelationModel = SecondModel.lstrip()
					
					if RelationModel.find("=")>-1:
					   RelationModel = (RelationModel[RelationModel.find("=")+1:].lstrip())
					relation_directory = DataCheck.set_relationmodel_path(self,AixLib_path, RelationModel, OriginalLibrary)
					SecondModel = SecondModel.lstrip()
					SecondModel = SecondModel.split(".")
					SecondModel = SecondModel[len(SecondModel) - 1]
					array1.append(x_array)
					y = array1[0][1].split('.')
					y = np.asarray(y)
					PolymorphismModel = y[len(y) - 1].split(';')
					PolymorphismModel = PolymorphismModel[0].split("(") 
					PolymorphismModel = PolymorphismModel[0]
					if relation_directory == None:
						continue
				   
					yield relation_directory + "," + RelationModel+","+Package
					
				
				if x_array[0] == "replaceable" and x_array[1] != "package" and x_array[1] != "model":
					Model = x_array[2]
					RelationModel = x_array[1]
					Package = (RelationModel)
					relation_directory = DataCheck.set_relationmodel_path(self,AixLib_path, RelationModel, OriginalLibrary)
					SecondModel = (line[line.find("constrainedby") + 13:line.find('"') - 1])
					RelationModel = SecondModel.lstrip()
					SecondModel = SecondModel.lstrip()
					SecondModel = SecondModel.split(".")
					SecondModel = SecondModel[len(SecondModel) - 1]
					array1.append(x_array)
					y = array1[0][1].split('.')
					y = np.asarray(y)
					PolymorphismModel = y[len(y) - 1].split(';')
					PolymorphismModel = PolymorphismModel[0].split("(") 
					PolymorphismModel = PolymorphismModel[0]
					if relation_directory == None:
						continue
					
					yield relation_directory + "," + RelationModel+","+Package
			
				if len(x_modelica)>2:
					if x_array[0] == "parameter" and x_modelica[1]!="SIunits"  and x_modelica[0]!="Medium" and x_modelica[1]!="Media":
						RelationModel= (x_array[1])
						relation_directory = DataCheck.set_relationmodel_path(self,AixLib_path, RelationModel, OriginalLibrary)
						if relation_directory == None:
							continue
						yield relation_directory + "," + RelationModel
				count = 0
				for i in range(0, len(self.ListLibrary), 1):
					count = count +1 
					x_modelica = x_array[0].split(".")
					Libraries = x_array[0].split(".")
					Libraries = Libraries[0]
				  
					if Libraries == self.ListLibrary[i] and x_array[0][9:16] != "SIunits": 
					  
						Model = x_array[0]
						if line.find("<")>-1:
						   Model= Model[0:line.find("<")-1]
						relation_directory = DataCheck.set_relationmodel_path(self,AixLib_path, Model, OriginalLibrary)
						if relation_directory == None:
							continue
						yield relation_directory + "," + Model
					elif count< len(self.ListLibrary):
						continue
					"""elif Libraries != self.ListLibrary[i] and x_modelica[0] != "Medium" :	
						ChildClass = filename_input.split(".")
						ChildClassStr = ""
						count = 0
						for w in ChildClass[0:2]:
							count = count + 1
							if count == 2:
								ChildClassStr =ChildClassStr+ w
							else:
								ChildClassStr =ChildClassStr+ w+"\\"
						RelationModel = x_array[0]
						T = filename_input.split("\\")
						T = (T[len(T)-1])
						T = T.split(".")
						x_Modelica = x_array[0].split(".")
						AixLib_path2 =AixLib_path+"\\"+T[0]+"\\"+T[1]
						Model = x_Modelica[len(x_Modelica)-1]
						relation_directory = DataCheck.showModel(AixLib_path2,Model)
						if relation_directory != None:
							#print(relation_directory)
							yield relation_directory + "," + RelationModel"""
				   
				"""for i in range(0, len(self.ListLibrary), 1):
					x_modelica = x_array[0].split(".")
					Libraries = x_array[0].split(".")
					Libraries = Libraries[0]
					if Libraries != self.ListLibrary[i] and x_modelica[0] != "Medium" :	
						
						ChildClass = filename_input.split(".")
						ChildClassStr = ""
						count = 0
						for w in ChildClass[0:2]:
							count = count + 1
							if count == 2:
								ChildClassStr =ChildClassStr+ w
							else:
								ChildClassStr =ChildClassStr+ w+"\\"
						RelationModel = x_array[0]
						T = filename_input.split("\\")
						T = (T[len(T)-1])
						T = T.split(".")
						x_Modelica = x_array[0].split(".")
						AixLib_path2 =AixLib_path+"\\"+T[0]+"\\"+T[1]
						Model = x_Modelica[len(x_Modelica)-1]
					   
						relation_directory = DataCheck.showModel(AixLib_path2,Model)
						if relation_directory != None:
							#print(relation_directory)
							yield relation_directory + "," + RelationModel
						else:
							continue"""
				
	
	def set_all_RelationModel(self, filename_input, output_path, AixLib_path):
		Test = []
		filename_extended = []
		while True:
			if filename_input != None:
				for z in Instanz.get_Relation(filename_input, AixLib_path):
					Model = Instanz.set_Relation(filename_input, AixLib_path)
					ClassDiagram.put_full_class(filename_input, output_path)
			
	def set_RelationModel(self, filename_input, AixLib_path):
		self.filename_input = filename_input
		readfile_in = open(self.filename_input, 'r+')
		array0 = [] 
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			if len(x_array) > 0:
				if x_array[0] == "extends":
					array0.append(x_array)
					RelationModel = (array0[0][1])
					RelationModel = RelationModel.lstrip()
					yield RelationModel
					pass
				if x_array[0] == "connect":
					array0.append(x_array)
					RelationModel = (array0[0][1])
					yield RelationModel 
					pass   
				if x_array[0] == "replaceable" and x_array[1] == "model":
					FirstModel = (line[line.find("=") + 1:line.find("constrainedby") - 1])
					yield FirstModel
					pass
				if x_array[0] == "replaceable" and x_array[1] == "package":
					if line.find("constrainedby") > -1:
						FirstModel = (line[line.find("=") + 1:line.find("constrainedby") - 1])
					yield FirstModel
					pass
				if x_array[0][0:8] == "Modelica" and x_array[0][9:16] != "SIunits" :
					if x_array[0].find("Interface") > -1 :
						Model = x_array[0].split(".")
						Model = (Model[len(Model) - 1])
					yield Model
					pass
   
	# Search and set connect 
	def setConnectinModel(self,filename_input, AixLib_path):
		self.ListLibrary = DataCheck.allModelicaLibrary(AixLib_path)
		readfile_in = open(filename_input, "r")
		for line in readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			if len(x_array) > 1:
				x_array[0] =  x_array[0].replace("("," ( ")
				if x_array[0] == "connect":
					Model1 = x_array[2].split(".")
					OutputModel = Model1[0]
					Outputport = Model1[1].replace(",","")
					Model2 = x_array[3].split(".")
					InputModel = Model2[0]
					Inputport = Model2[1].replace(",","")
					relation = OutputModel +' "'+Outputport+'"'+ " #-# " +'"'+Inputport+'" ' +InputModel + " : >"
					yield relation
					continue
					pass
					

if __name__ == "__main__": 
	from Object_Oriented_Relations import Relation
	Instanz = Relation(AixLib_path)
	# DataCheck = General.DataCheck
	#filename_input = r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\tempdata\PartialExpansionValve.java"
