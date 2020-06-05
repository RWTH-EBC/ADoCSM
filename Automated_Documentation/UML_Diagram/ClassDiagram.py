
import linecache
import numpy as np


from General import DataCheck

class ClassDiagram(object):
	def __init__(self):
		print("add variables like aixlib_path")
	
	def set_import(self,filename_input):
		self.readfile_in = open(filename_input,'r')
		for line in self.readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
			if len(x_array)>0 :
				if x_array[0] =="import":
					self.contraction = x_array[1] 
					self.original = x_array[3]
					self.gesamt= self.contraction+ ","+ self.original
					#yield self.gesamt
					self.gesamt=self.gesamt.split(",")
				  
					return self.gesamt
	
	################################################################################################################################################################################################
	#Find and write public attributes in PlantUML format	 
	def set_Attribute_public(self,filename_input,  filename_output ,output_path,parameter,variables,primitivevariables,complexvariables,Relation,showconstant):
		counter_import = []
		self.readfile_in = open(filename_input,'r+')
		readfile_out = open(filename_output,"w")
		array01 = []
		arraypoly = []
		Counter_Protected = []
		Counter_Equation = []
		counter = 1
		for line in self.readfile_in.readlines():
			Counter_Protected.append(counter)
			counter = counter +1
			line = line.replace('(',' { ')
			line = line.replace(')',' } ')
			line = line.replace('[',' [ ')
			line = line.replace(']',' ] ')
			line = line.replace(';','')
			line = line.replace(' = ','=')
			x = line.split()
			x_array = np.asarray(x)
			if line.find("protected")==0:
				break
			if line.find("equation")==0:
				break
			if len(x_array)>0 :
				x_modelica = x_array[0].split(".")
				x_medium = x_array[0].split(".")
	
				################################################################################################################################################################################################
				#Shows relations in class with initial values
				if Relation == True:
					if x_array[0] == "extends":
						if line.find("{")>-1:
							array01.append(line)
							pass
					if x_array[0] == "replaceable":
						array01.append(line)
						arraypoly.append(x_array[2])
					if len(arraypoly)>0:
						if arraypoly[0]==x_array[0]:
							array01.append(line)
					if x_modelica[0] == "Modelica" and x_modelica[1] != "SIunits" and x_modelica[1] != "Blocks": 
						array01.append(line)
						pass
			   
				################################################################################################################################################################################################
				##show Parameter
				if parameter == True:
					if x_array[0] == "parameter":
						array01.append(line)
						pass
				
				################################################################################################################################################################################################
				##show complexvariables
				if complexvariables == True:
					if x_medium[0] == "Medium":
						array01.append(line)
						pass
				if complexvariables == True:
					if x_modelica[0] == "Modelica" and x_modelica[1] == "Blocks":
						array01.append(line)
						pass
				
				################################################################################################################################################################################################
				##show Variables: SIUnits
				if x_modelica[0] == "Modelica":
					if variables == True:
						if x_modelica[1] == "SIunits":
							array01.append(line)
							pass
				 
				################################################################################################################################################################################################
				##show primitivev ariables
				if primitivevariables == True:   
					if x_array[0] == "Real":
					   array01.append(line)
					   pass
				if primitivevariables == True:   
					if x_array[0] =="input":
					   array01.append(line)
					   pass
				if primitivevariables == True: 
					if x_array[0] =="stream":
						array01.append(line)
						pass
				if primitivevariables == True:   
					if x_array[0] =="flow":
						array01.append(line)
						pass
				if primitivevariables == True:	   
					if x_array[0] == "final":
						array01.append(line)
						pass
				if primitivevariables == True:	   
					if x_array[0] == "String":
						array01.append(line)
						pass
				if primitivevariables == True:	   
					if x_array[0] == "Integer":
						array01.append(line)
						pass
				if primitivevariables == True:	   
					if x_array[0] == "Boolean":
						array01.append(line)
						pass
				if primitivevariables == True:	   
					if x_array[0] == "RealInput":
						array01.append(line)
						pass
				if primitivevariables == True:	   
					if x_array[0] == "RealOutput":
						array01.append(line)
						pass
			  
				################################################################################################################################################################################################
				##show Constants
				if showconstant == True:   
					if x_array[0] =="constant":
						array01.append(line)
						pass
			continue
			pass
		
		######################################################################################
		##Write public attributes
		i=0
		while i<len(array01):
			a = array01[i].find('annotation')
			x = array01[i].find('=')
			q = array01[i].find('"')
			w = array01[i].find('"',q+1,a)
			w = array01[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array01[i][0:w]))
			else: 
			   readfile_out.write(("\n + "+ array01[i][0:q]))
			i = i+1
		"""
		##Medium
		##################################################################################### 
		i = 0
		while i<len(array02):
			a = array02[i].find('annotation')
			x = array02[i].find('=')
			q = array02[i].find('"')
			w = array02[i].find('"',q+1,a)
			w = array02[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array02[i][0:w]))
			else: 
			   readfile_out.write(("\n + "+ array02[i][0:q]))
			i = i+1
		##Modelica.SiUnits	
		######################################################################################
		i = 0
		while i<len(array03):
			a = array03[i].find('annotation')
			x = array03[i].find('=')
			q = array03[i].find('"')
			w = array03[i].find('"',q+1,a)
			w = array03[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array03[i][0:w]))
			else: 
			   readfile_out.write(("\n + "+ array03[i][0:q]))
			i = i+1
		
		##Real
		######################################################################################
		i = 0
		while i<len(array04):
			a = array04[i].find('annotation')
			x = array04[i].find('=')
			q = array04[i].find('"')
			w = array04[i].find('"',q+1,a)
			w = array04[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array04[i][0:w]))
			
			else: 
			   readfile_out.write(("\n + "+ array04[i][0:q]))
			i = i+1
		
		##Modelica.Block
		########################################################################################
		i = 0
		while i<len(array05):
			a = array05[i].find('annotation')
			x = array05[i].find('=')
			q = array05[i].find('"')
			w = array05[i].find('"',q+1,a)
			w = array05[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array05[i][0:w]))
			
			else: 
			   readfile_out.write(("\n + "+ array05[i][0:q]))
			i = i+1
		
		##Input
		#######################################################################################
		i = 0
		while i<len(array06):
			a = array06[i].find('annotation')
			x = array06[i].find('=')
			q = array06[i].find('"')
			w = array06[i].find('"',q+1,a)
			w = array06[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array06[i][0:w]))
			
			else: 
			   readfile_out.write(("\n + "+ array06[i][0:q]))
			i = i+1
		## Stream
		#################################################################################
		i = 0
		while i<len(array07):
			a = array07[i].find('annotation')
			x = array07[i].find('=')
			q = array07[i].find('"')
			w = array07[i].find('"',q+1,a)
			w = array07[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n + "+ array07[i][0:w]))
			else: 
			   readfile_out.write(("\n + "+ array07[i][0:q]))
			i = i+1
		##flow
		###################################################################################
		i = 0
		while i<len(array08):
			a = array08[i].find('annotation')
			x = array08[i].find('=')
			q = array08[i].find('"')
			w = array08[i].find('"',q+1,a)
			w = array08[i].find('"',w+1,a)
			if w >-1:
				readfile_out.write(("\n + "+ array08[i][0:w]))
			else: 
				readfile_out.write(("\n + "+ array08[i][0:q]))
			i = i+1
		##constant
		####################################################################################
		i = 0
		while i<len(array09):
			a = array09[i].find('annotation')
			x = array09[i].find('=')
			q = array09[i].find('"')
			w = array09[i].find('"',q+1,a)
			w = array09[i].find('"',w+1,a)
			if w >-1:
				readfile_out.write(("\n + "+ array09[i][0:w]))
			else: 
				readfile_out.write(("\n + "+ array09[i][0:q]))
			i = i+1
		##final
		####################################################################################	
		i = 0   
		while i<len(array10):
			a = array10[i].find('annotation')
			x = array10[i].find('=')
			q = array10[i].find('"')
			w = array10[i].find('"',q+1,a)
			w = array10[i].find('"',w+1,a)
			if w >-1:
				readfile_out.write(("\n + "+ array10[i][0:w]))
			else: 
				readfile_out.write(("\n + "+ array10[i][0:q]))
			i = i+1"""
   
		
		
		self.readfile_in.close()
		readfile_out.close() 
		return Counter_Protected
		
	 
	################################################################################################################################################################################################
	#Find and write protected attributes in PlantUML format  
	def set_Attribute_protected(self,filename_input,  filename_output ,output_path,parameter,variables,primitivevariables,complexvariables,showconstant):
		
		#Counter_Protected = Instanz.set_Attribute_public(filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables)
		self.readfile_in = open(filename_input,'r+')
		readfile_out = open(filename_output,"a")
		array01 = []
		Counter_Equation = []
		counter = 0
		for line in self.readfile_in.readlines():
			counter = counter +1
			if line.find("protected")==0:
				Counter_Equation.append(counter)
				continue
			if line.find("initial equation")==0:
				Counter_Equation.append(counter)
				break
			if line.find("equation")==0:
				Counter_Equation.append(counter)
				break
			if line.find("public")==0:
				Counter_Equation.append(counter)
				break
			if line.find("algorithm")==0:
				Counter_Equation.append(counter)
				break
			if line.find("annotation")==0:
				Counter_Equation.append(counter)
				break
		 
		################################################################################################################################################################################################
		#Find and write protected attributes in thsi area	
		if len(Counter_Equation)>1:
			for i in range(Counter_Equation[0],Counter_Equation[1],1):
				line = (linecache.getline(filename_input, i)) 
				line = line.replace('(',' { ')
				line = line.replace(')',' } ')
				line = line.replace('[',' [ ')
				line = line.replace(']',' ] ')
				line = line.replace(';','')
				line = line.replace(' = ','=')
				x = line.split()		 
				x_array = np.asarray(x)
			   
				if len(x_array)>0 :
					x_modelica = x_array[0].split(".")
					x_medium = x_array[0].split(".")
				
					################################################################################################################################################################################################
					##show Parameter
					if parameter == True:
						if x_array[0] == "parameter":
							array01.append(line)
							pass
					
					################################################################################################################################################################################################
					##show complex variables
					if complexvariables == True:
						if x_medium[0] == "Medium":
							array01.append(line)
							pass
					if complexvariables == True:		 
						if x_modelica[0] == "Modelica" and x_modelica[1] == "SIunits":
							if variables == True:
								array01.append(line)
								pass
					if complexvariables == True:
						if x_modelica[0] == "Modelica" and x_modelica[1] == "Blocks":
							array01.append(line)
							pass
					
					################################################################################################################################################################################################
					##show primitive variables 
					if primitivevariables == True:
						if x_array[0] == "Real":
							array01.append(line)
							pass
					if primitivevariables == True:
						if x_modelica[0] =="input":
							array01.append(line)
					if primitivevariables == True:
						if x_array[0] =="stream":
							array01.append(line)
					if primitivevariables == True:
						if x_array[0] =="flow":
							array01.append(line)
					
					if primitivevariables == True:	   
						if x_array[0] == "final":
							array01.append(line)
							pass
					if primitivevariables == True:	   
						if x_array[0] == "String":
							array01.append(line)
							pass
					if primitivevariables == True:	   
						if x_array[0] == "Integer ":
							array01.append(line)
							pass
					if primitivevariables == True:	   
						if x_array[0] == "Boolean  ":
							array01.append(line)
							pass
					if primitivevariables == True:	   
						if x_array[0] == "RealInput":
							array01.append(line)
							pass
					if primitivevariables == True:	   
						if x_array[0] == "RealOutput":
							array01.append(line)
							pass
			  
					
					################################################################################################################################################################################################
					##show Constants 
					if showconstant == True:
						if x_array[0] =="constant":
							array01.append(line)
				continue
				pass
		
		######################################################################################
		##Write protected attributes
		i=0
		while i<len(array01):
			a = array01[i].find('annotation')
			x = array01[i].find('=')
			q = array01[i].find('"')
			w = array01[i].find('"',q+1,a)
			w = array01[i].find('"',w+1,a)
			
			if w >-1:
				 readfile_out.write(("\n # "+ array01[i][0:w]))
				 
			else: 
			   readfile_out.write(("\n # "+ array01[i][0:q]))
			i = i+1
		""" ##Medium
		######################################################################################
		i = 0
		while i<len(array02):
			a = array02[i].find('annotation')
			x = array02[i].find('=')
			q = array02[i].find('"')
			w = array02[i].find('"',q+1,a)
			w = array02[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array02[i][0:w]))
			
			else: 
			   readfile_out.write(("\n # "+ array02[i][0:q]))
			i = i+1
		##Modelica.SiUnits
		#########################################################################################
		i = 0
		while i<len(array03):
			a = array03[i].find('annotation')
			x = array03[i].find('=')
			q = array03[i].find('"')
			w = array03[i].find('"',q+1,a)
			w = array03[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array03[i][0:w]))
			
			else: 
			   readfile_out.write(("\n # "+ array03[i][0:q]))
			i = i+1
		#Real
		###################################################################################
		i = 0
		while i<len(array04):
			a = array04[i].find('annotation')
			x = array04[i].find('=')
			q = array04[i].find('"')
			w = array04[i].find('"',q+1,a)
			w = array04[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array04[i][0:w]))
			
			else: 
			   readfile_out.write(("\n # "+ array04[i][0:q]))
			i = i+1
		##################################################################################
		##Modelica.Block
		i = 0
		while i<len(array05):
			a = array05[i].find('annotation')
			x = array05[i].find('=')
			q = array05[i].find('"')
			w = array05[i].find('"',q+1,a)
			w = array05[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array05[i][0:w]))
			
			else: 
			   readfile_out.write(("\n # "+ array05[i][0:q]))
			i = i+1
		##Input
		###################################################################################
		i = 0
		while i<len(array06):
			a = array06[i].find('annotation')
			x = array06[i].find('=')
			q = array06[i].find('"')
			w = array06[i].find('"',q+1,a)
			w = array06[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array06[i][0:w]))
			
			else: 
				readfile_out.write(("\n # "+ array06[i][0:q]))
			i = i+1
		##Stream
		######################################################################################
		i = 0
		while i<len(array07):
			a = array07[i].find('annotation')
			x = array07[i].find('=')
			q = array07[i].find('"')
			w = array07[i].find('"',q+1,a)
			w = array07[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array07[i][0:w]))
			
			else: 
				readfile_out.write(("\n # "+ array07[i][0:q]))
			i = i+1
		##flow
		######################################################################################
		i = 0
		while i<len(array08):
			a = array08[i].find('annotation')
			x = array08[i].find('=')
			q = array08[i].find('"')
			w = array08[i].find('"',q+1,a)
			w = array08[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array08[i][0:w]))
			
			else: 
				readfile_out.write(("\n # "+ array08[i][0:q]))
			i = i+1
		##constant
		######################################################################################
		i = 0
		while i<len(array09):
			a = array09[i].find('annotation')
			x = array09[i].find('=')
			q = array09[i].find('"')
			w = array09[i].find('"',q+1,a)
			w = array09[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array09[i][0:w]))
			
			else: 
				readfile_out.write(("\n # "+ array09[i][0:q]))
			i = i+1
		##final
		######################################################################################
		while i<len(array10):
			a = array10[i].find('annotation')
			x = array10[i].find('=')
			q = array10[i].find('"')
			w = array10[i].find('"',q+1,a)
			w = array10[i].find('"',w+1,a)
			if w >-1:
				 readfile_out.write(("\n # "+ array10[i][0:w]))
			
			else: 
				readfile_out.write(("\n # "+ array10[i][0:q]))
			i = i+1"""
		
		self.readfile_in.close()
		readfile_out.close()
		return Counter_Equation 
	
	################################################################################################################################################################################################
	#Searches and Writes Initial Methods in PlantUML Format
	def set_initialMethode(self,filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode):
		self.readfile_in = open(filename_input,'r')
		readfile_out = open(filename_output,"a")
		array_if = []
		array1_if = []
		array_elseif = []
		array_else = []
		array_endif = []
		array_equationsign = []
		array_for = []
		
		Countlistfor = []
		Countlistif = []
		Countlistelseif = []
		Countlistelse = []
		countlistendif =[]
		Counter_Equation = []
		countlistendif = []
		counter = 0
		Counter_InitialEquation = []
		count = []
		counter = 0
		for line in self.readfile_in.readlines():
			counter = counter +1
			if line.find("initial equation")==0 :
				Counter_InitialEquation.append(counter)
				continue
			if line.find("equation")==0:
				Counter_InitialEquation.append(counter)
				break
			if line.find("annotation")==0:
				Counter_InitialEquation.append(counter)
				break
		
		if len(Counter_InitialEquation)>1:
			count = Counter_InitialEquation[0]
			for i in range(Counter_InitialEquation[0],Counter_InitialEquation[1],1):
				count = count +1
				line = linecache.getline(filename_input, i)
				line = line.replace(";"," ; ")
				line = line.replace(" = ","=")
				line = line.replace("\n"," ")
							
				x = line.split()		 
				x_array = np.asarray(x)
				if len(x_array)>0:
					if methode ==True:
						#############################################################################
						## if-Conditions
						if x_array[0] == "if" and len(countlistendif)==0:
							
							x = line.find('"')
							array_if.append(line[:x-1])
							Countlistif.append(count)
							countlistendif.append(count) 
							continue
						elif len(Countlistif)==1 and len(Countlistelseif)==0 and len(countlistendif)==1: 
							if x_array[0] != "if" and  x_array[0] != "elseif"and  x_array[0] != "else" and  x_array[1] != "if;":
								x = line.find('"')
								array_if.append(line[:x-1])	
								continue
						#############################################################################
						## elseif
							elif x_array[0]=="elseif":
								
								x = line.find('"')
								array_elseif.append(line[:x-1])	
								Countlistelseif.append(count)
								array_ifstr =""
								###Write if-Conditions
								if len(array_if)>0:
									for i in array_if:
										array_ifstr=array_ifstr+(i)+";"
										continue
									readfile_out.write("\n # "+"("+array_ifstr+")")
									Countlistif = []
								continue
							elif x_array[0]=="else":
								x = line.find('"')
								Countlistelse.append(count)
								array_else.append(line[:x-1])	
								array_ifstr =""
								###Write if-Conditions
								if len(array_if)>0:
									for i in array_if:
										array_ifstr=array_ifstr+(i)+";"
										continue
									readfile_out.write("\n # "+"("+array_ifstr+")")
									Countlistif = []
								continue
						

						elif len(Countlistif) == 0 and len(Countlistelseif)>0 and len(Countlistelse)==0 and len(countlistendif)==1:
						  
							if x_array[0] != "if" and  x_array[0] != "elseif" and x_array[0] != "else" and  x_array[1] != "if;" and x_array[1] != "if" :
								x = line.find('"')
								array_elseif.append(line[:x-1])   
								continue
							elif x_array[0] == "if" and   x_array[1] != "if;" and x_array[1] != "if" :
								x = line.find('"')
								array_elseif.append(line[:x-1])   
								continue
							
							
							
							elif x_array[0]=="elseif" and len(array_elseif)>0:
								
								x = line.find('"')
								array_elifstr = ""
								if len(array_elseif)>0:
									for i in array_elseif:
										array_elifstr=array_elifstr+(i)+";"
									readfile_out.write("\n # "+"("+array_elifstr+")")
									array_elseif = []
								array_elseif.append(line[:x-1])
								continue
							elif x_array[0]=="elseif" and len(array_elseif)==0:
							   
								x = line.find('"')
								array_elseif.append(line[:x-1])   
								continue
							elif x_array[0]=="else" and len(array_elseif)>0:
								x = line.find('"')
								array_else.append(line)   
								array_elifstr = ""
								Countlistelse.append(count)
								###Write elseif-Conditions
								if len(array_elseif)>0:
									for i in array_elseif:
										array_elifstr=array_elifstr+(i)
									readfile_out.write("\n # "+"("+array_elifstr+")")
									Countlistelseif = []
								continue
							elif x_array[0]=="end" and x_array[1]=="if":
								x = line.find('"')
							   
								Countlistelse.append(count)
								array_else.append(line[:x-1])	
								array_ifstr =""
								
								###Write if-Conditions
								if len(array_elseif)>0:
									for i in array_elseif:
										array_ifstr=array_ifstr+(i)+";"
									readfile_out.write("\n # "+"("+array_ifstr+")")
								readfile_out.write("\n # "+"("+line+")")
								Countlistelseif = []
								Countlistelse = []
								array_if = []
								array_elseif =[]
								array_else = []
								array_endif = []
								countlistendif = []
								continue
						elif len(Countlistelseif) == 0 and len(Countlistelse)==1 and len(countlistendif)==1:
						  
							if x_array[0]=="else":
								#x = line.find('"')
								#array_else.append(line[:x-1])  
								continue
							elif x_array[0]=="end" and x_array[1]=="if":
								x = line.find('"')
								array_endif.append(line[:x-1])
								array_elsestr=""
								if len(array_else)>0:
									for i in array_else:
										array_elsestr = array_elsestr+(i)+";"
									readfile_out.write("\n # "+"("+array_elsestr+")")
								readfile_out.write("\n # "+"("+array_endif[0]+")")
								Countlistelseif = []
								Countlistelse = []
								array_if = []
								array_elseif =[]
								array_else = []
								array_endif = []
								countlistendif = []
								continue
							else:
								x = line.find('"')
								array_else.append(line[:x-1]) 
								continue
							   
						
						 #############################################################################
						 ## end for
						elif x_array[0]=="for" or len(Countlistfor)>0:
							x = line.find('"')
							Countlistfor.append(count)
							array_for.append(line[:x-1])
							x = line.find('"')
							if x_array[0]=="end":
								if len(array_for)>0:
									array_forstr=""
									for i in array_for:
										array_forstr = array_forstr+(i)+";"
									readfile_out.write("\n # "+"("+array_forstr+")")
									Countlistfor = []
									array_for = []
							else:
								continue
						#assert
						################################################################################################################################
						elif x_array[0]=="assert":
							readfile_out.write("\n # "+"("+line+")")
							
					   
						##############################################################################
						####Equation sign  
						elif line.find("=")>-1:
							x = line.find('"')
							y = line.find('=')
							readfile_out.write("\n # "+line[:y-1]+"("+line[y+1:x].replace(";","")+")")
							continue
			
	   
	   
		
		self.readfile_in.close()
		readfile_out.close()
	
	################################################################################################################################################################################################
	#Searches and Writes Methods in PlantUML Format   
	def set_Methode(self,filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode):
		self.readfile_in = open(filename_input,'r')
		readfile_out = open(filename_output,"a")
		array_if = []
		array1_if = []
		array_elseif = []
		array_else = []
		array_endif = []
		array_equationsign = []
		array_for = []
		
		Countlistfor = []
		Countlistif = []
		Countlistelseif = []
		Countlistelse = []
		Counter_Equation = []
		countlistendif = []
		counter = 0
		for line in self.readfile_in.readlines():
			counter = counter +1
			if line.find("equation")==0:
				Counter_Equation.append(counter)
				continue
			if line.find("annotation")==0:
				Counter_Equation.append(counter)
				break
		if len(Counter_Equation)>1:
			count = Counter_Equation[0]
			
			for i in range(Counter_Equation[0],Counter_Equation[1],1):
				count = count +1
				line = linecache.getline(filename_input, i)
				line = line.replace(";"," ; ")
				line = line.replace(" = ","=")
				line = line.replace("\n"," ")
							
				x = line.split()		 
				x_array = np.asarray(x)
				if len(x_array)>0:
					if methode ==True:
						#############################################################################
						## if-Conditions
						if x_array[0] == "if":
							x = line.find('"')
							array_if.append(line[:x-1])
							Countlistif.append(count)
							continue
						elif len(Countlistif)==1 and len(Countlistelseif)==0: 
							if x_array[0] != "if" and  x_array[0] != "elseif"and  x_array[0] != "else" and  x_array[1] != "if;":
								x = line.find('"')
								array_if.append(line[:x-1])	
								continue
						#############################################################################
						## elseif
							elif x_array[0]=="elseif":
								x = line.find('"')
								array_elseif.append(line[:x-1])	
								Countlistelseif.append(count)
								array_ifstr =""
								###Write if-Conditions
								if len(array_if)>0:
									for i in array_if:
										array_ifstr=array_ifstr+(i)+";"
										continue
									readfile_out.write("\n + "+"("+array_ifstr+")")
									Countlistif = []
								continue
							elif x_array[0]=="else":
								x = line.find('"')
								Countlistelse.append(count)
								array_else.append(line[:x-1])	
								array_ifstr =""
								###Write if-Conditions
								if len(array_if)>0:
									for i in array_if:
										array_ifstr=array_ifstr+(i)+";"
										continue
									readfile_out.write("\n + "+"("+array_ifstr+")")
									Countlistif = []
								continue

						elif len(Countlistif) == 0 and len(Countlistelseif)>0 and len(Countlistelse)==0:
							if x_array[0] != "if" and  x_array[0] != "elseif" and x_array[0] != "else" and  x_array[1] != "if;" and x_array[1] != "if" :
								x = line.find('"')
								array_elseif.append(line[:x-1])   
								continue
							elif x_array[0]=="elseif" and len(array_elseif)>0:
								x = line.find('"')
								#array_elseif.append(line[:x-1])  
								array_elifstr = ""
								###Write elseif-Conditions
								if len(array_elseif)>0:
									for i in array_elseif:
										array_elifstr=array_elifstr+(i)+";"
									readfile_out.write("\n + "+"("+array_elifstr+")")
									array_elseif = []
								array_elseif.append(line[:x-1])
								continue
							elif x_array[0]=="elseif" and len(array_elseif)==0:
								x = line.find('"')
								array_elseif.append(line[:x-1])   
								continue
							#elif len(array_elseif)>0:
							 #   x = line.find('"')
							  #  array_elseif.append(line[:x-1])
							   # continue
							elif x_array[0]=="else" and len(array_elseif)>0:
								x = line.find('"')
								array_else.append(line)   
								array_elifstr = ""
								Countlistelse.append(count)
								###Write elseif-Conditions
								if len(array_elseif)>0:
									for i in array_elseif:
										array_elifstr=array_elifstr+(i)
									readfile_out.write("\n + "+"("+array_elifstr+")")
									Countlistelseif = []
								continue
						elif len(Countlistelseif) == 0 and len(Countlistelse)==1:
						  
							if x_array[0]=="else":
								#x = line.find('"')
								#array_else.append(line[:x-1])  
								continue
							elif x_array[0]=="end" and x_array[1]=="if":
								x = line.find('"')
								array_endif.append(line[:x-1])
								array_elsestr=""
								if len(array_else)>0:
									for i in array_else:
										array_elsestr = array_elsestr+(i)+";"
									readfile_out.write("\n + "+"("+array_elsestr+")")
								readfile_out.write("\n + "+"("+array_endif[0]+")")
								Countlistelseif = []
								Countlistelse = []
								array_if = []
								array_elseif =[]
								array_else = []
								array_endif = []
								continue
							else:
								x = line.find('"')
								array_else.append(line[:x-1]) 
								continue
							   
						
						 #############################################################################
						 ## end for
						elif x_array[0]=="for" or len(Countlistfor)>0:
							x = line.find('"')
							Countlistfor.append(count)
							array_for.append(line[:x-1])
							x = line.find('"')
							if x_array[0]=="end":
								if len(array_for)>0:
									array_forstr=""
									for i in array_for:
										array_forstr = array_forstr+(i)+";"
									readfile_out.write("\n + "+"("+array_forstr+")")
									Countlistfor = []
									array_for = []
							else:
								continue
						#assert
						################################################################################################################################
						elif x_array[0]=="assert":
							readfile_out.write("\n + "+"("+line+")")
							
					   
						##############################################################################
						####Equation sign  
						elif line.find("=")>-1:
							x = line.find('"')
							y = line.find('=')
							readfile_out.write("\n + "+line[:y-1]+"("+line[y+1:x].replace(";","")+")")
							continue
		self.readfile_in.close()
		readfile_out.close()
		
	
	
	
	
	def insert_line(self,filename_input, output_path,insert_pos, line):
		filename_output = DataCheck.setUMLModell(self,filename_input, output_path)
		f = open(filename_output,"r+")
		lines = f.readlines()
		f.close()
		lines.insert(insert_pos, line)
		f = open(filename_output, 'w')
		f.writelines(lines)
		f.close()
		return filename_output
	   
	 
	def number_of_lines(self,filename_input,output_path):
		self.filename = DataCheck.setUMLModell(self,filename_input, output_path)
		file = open(self.filename,"r")
		lines = file.readlines()
		numberLines =  len(lines)
		return numberLines
		file.close()
		 
	######################################################################################################
	#Sets the class name and stereotypes
	def ClassName(self,filename_input,Package,showType):
		self.readfile_in = open(filename_input,'r')
		stereotyp=[]
		for line in self.readfile_in.readlines():
			x = line.split()
			x_array = np.asarray(x)
		###################################################################################################
		#Stereotype
			if len(Package)==0 :
				if len(x_array)>0:
					if x_array[0] == 'class':
						stereotyp.append(x_array)
						classname = " class "+stereotyp[0][1] + " << " +stereotyp[0][0] + " >>  {"
						return classname
					if x_array[0] == 'function':
						stereotyp.append(x_array)
						classname = " class "+stereotyp[0][1] + " << " +stereotyp[0][0] + " >>  {"
						return classname
					if x_array[0] == 'partial' and x_array[1]=="connector":
						stereotyp.append(x_array)
						classname= " interface "+stereotyp[0][2] + " << " +stereotyp[0][0] +" "+ stereotyp[0][1]+ " >>  {"
						return classname
					"""if x_array[0] == 'package' :
						T = filename_input.split(".")
						T = T[len(T)-2]
						stereotyp.append(x_array)
						classname= " package "+stereotyp[0][2].replace('"',"") + " << " +stereotyp[0][0]+ " >>  {" 
						return classname"""
					if x_array[0] == 'partial':
						stereotyp.append(x_array)
						classname= " Class "+stereotyp[0][2] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "model":
						stereotyp.append(x_array)
						classname = "Class "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "block":
						stereotyp.append(x_array)
						classname = "Class "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "connector":
						stereotyp.append(x_array)
						classname = "interface "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "type":
						x = line.find("(")
						y = line.find(",")
						z = line.find(",",y+1)
						w = line.find("annotation",z+1)
						stereotyp.append(x_array)
						if showType == True:
							classname = "enum	 "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {\n" +line[x:y]+"\n"+line[y:z]+"\n"+line[z:w]
						else:
							classname = "enum	 "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >> {" 
						return classname
					if x_array[0] == "record":
						stereotyp.append(x_array)
						classname = "class	 "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
			
			##for Replaceable Packages or Models
			if len(Package)>0:
				if len(x_array)>0:
					if x_array[0] == 'class':
						stereotyp.append(x_array)
						classname= "package "+ Package[0].replace('"',"") +"{ \n"+ "class "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == 'function':
						stereotyp.append(x_array)
						classname= "package "+ Package[0].replace('"',"") +"{ \n"+ "class "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						
						return classname
					if x_array[0] == 'type':
						stereotyp.append(x_array)
						classname= "package "+ Package[0].replace('"',"") +"{ \n"+ "enum "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == 'partial':
						stereotyp.append(x_array)
						classname= "package "+ Package[0].replace('"',"") +"{ \n"+ "class "+stereotyp[0][2] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "model":
						stereotyp.append(x_array)
						classname = "package "+ Package[0].replace('"',"") +"{ \n"+"\n"+"Class "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "block":
						stereotyp.append(x_array)
						classname = "package "+ Package[0].replace('"',"") +"{ \n"+"\n"+"Class "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "connector":
						stereotyp.append(x_array)
						classname = "package "+ Package[0].replace('"',"") +"{\n"+"interface "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
					if x_array[0] == "type":
						x = line.find("(")
						y = line.find(",")
						z = line.find(",",y+1)
						w = line.find("annotation",z+1)
						stereotyp.append(x_array)
						classname = "enum	 "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {\n" +line[x:y]+"\n"+line[y:z]+"\n"+line[z:w]
						return classname
					if x_array[0] == "record":
						stereotyp.append(x_array)
						classname ="package "+ Package[0] +"{\n"+ "class	 "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
						return classname
			self.readfile_in.close()
	
	###################################################################################		
	##Merge the individual model text files into an entire text file
	def Appender(self,output_path,finalData):
		destination  = output_path
		suffixes = []
		for path in Path(destination).iterdir():
			if path.is_file():
				suffixes.append(output_path+"\\"+path.stem+path.suffix)
		filename_input = open(finalData,"w")
		for i in range(0,len(suffixes)):
			input = open(suffixes[i],"r")
			for line in input:
				line = (line.replace("@startuml",""))
				line = (line.replace("@enduml",""))
				filename_input.write(line)
			input.close()  
		Instanz.insert_line
		filename_input.close()
		  
	  
	
	def put_full_class(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType):
		filenamelist = []
		filename_output = DataCheck.setUMLModell(self,filename_input, output_path)
		Instanz.set_Attribute_public(filename_input,filename_output, output_path,parameter,variables,primitivevariables,complexvariables,Relation,showconstant)			
		Instanz.set_Attribute_protected(filename_input, filename_output,output_path,parameter,variables,primitivevariables,complexvariables,showconstant)
		Instanz.set_initialMethode(filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
		Instanz.set_Methode(filename_input, filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
		
		if Instanz.ClassName(filename_input,Package,showType)!=None:#   Instanz.insert_line(filename_input,output_path, 1,"\n"+i )
			if len(Package)==0:
				Instanz.insert_line(filename_input,output_path, 0, "@startuml")
				Instanz.insert_line(filename_input,output_path,Instanz.number_of_lines(filename_input,output_path),"\n"+"}"+ "\n"+ "@enduml")
				Instanz.insert_line(filename_input,output_path, 1,"\n"+"\n"+"\n"+"\n"+ Instanz.ClassName(filename_input,Package,showType)+"\n") 
			if len(Package)>0 :
				
				Packages = (Package[0].split("."))
				PackageStr = ""
				count = 0
				for w in Packages[0:len(Packages)-1]:
					if count == 0:
						PackageStr = PackageStr +w
					else:
						PackageStr = PackageStr +"."+w
					count = count +1
				Package = []
				Package.append(PackageStr)
				filename_input2 =filename_input.split(".")
				filename_input2str = ""
				count = 0
				for x in filename_input2:
					count = count +1
					if count == len(filename_input2)-1:
						continue 
					if count == len(filename_input2): 
						filename_input2str = filename_input2str +x
					else:
						filename_input2str = filename_input2str +x+"."
				Instanz.insert_line(filename_input,output_path, 0, "@startuml")
				Instanz.insert_line(filename_input,output_path,Instanz.number_of_lines(filename_input,output_path),"\n"+"}"+ "\n"+"}"+"\n"+ "@enduml")
				Instanz.insert_line(filename_input,output_path, 1,"\n"+"\n"+"\n"+"\n"+ Instanz.ClassName(filename_input,Package,showType)+"\n") 
				filename_input2 =  filename_input2str
				if showPackages==True:
					filename_package = DataCheck.set_ModelsinPackages(self,filename_input2, output_path)
					if filename_input in filename_package:
						filename_package.remove(filename_input)
					for i in range(0,len(filename_package)-1,1):
						filename_output = DataCheck.setUMLModell(self,filename_package[i], output_path)
						Instanz.set_Attribute_public(filename_package[i],filename_output, output_path,parameter,variables,primitivevariables,complexvariables,Relation,showconstant)			
						Instanz.set_Attribute_protected(filename_package[i], filename_output,output_path,parameter,variables,primitivevariables,complexvariables,showconstant)
						Instanz.set_initialMethode(filename_package[i],filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
						Instanz.set_Methode(filename_package[i], filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
						Instanz.insert_line(filename_package[i],output_path, 0, "@startuml")
						Instanz.insert_line(filename_package[i],output_path,Instanz.number_of_lines(filename_package[i],output_path)+1,"\n"+"}"+ "\n"+"}"+"\n"+ "@enduml")
						if Instanz.ClassName(filename_package[i],Package,showType)!=None:
							Instanz.insert_line(filename_package[i],output_path, 1,"\n"+"\n"+ Instanz.ClassName(filename_package[i],Package,showType)+"\n") 
						filenamelist.append(filename_package[i])
	   
		return filenamelist
	
	def put_full_classPackage(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package):
		filename_output = DataCheck.setUMLModell(self,filename_input, output_path)
		Instanz.set_Attribute_public(filename_input,filename_output, output_path,parameter,variables,primitivevariables,complexvariables)			
		Instanz.set_Attribute_protected(filename_input, filename_output,output_path,parameter,variables,primitivevariables,complexvariables)
		Instanz.set_initialMethode(filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
		Instanz.set_Methode(filename_input, filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
		if Instanz.ClassName(filename_input,Package)!=None:#   Instanz.insert_line(filename_input,output_path, 1,"\n"+i )
			if len(Package)==0:
				Instanz.insert_line(filename_input,output_path, 0, "@startuml")
				Instanz.insert_line(filename_input,output_path,Instanz.number_of_lines(filename_input,output_path),"\n"+"}"+ "\n"+ "@enduml")
				Instanz.insert_line(filename_input,output_path, 1,"\n"+"\n"+"\n"+"\n"+ Instanz.ClassName(filename_input,Package)+"\n") 
			if len(Package)>0:
				Packages = (Package[0].split("."))
				PackageStr = ""
				count = 0
				for w in Packages[0:len(Packages)-1]:
					if count == 0:
						PackageStr = PackageStr +w
					else:
						PackageStr = PackageStr +"."+w
					count = count +1
				Package = []
				Package.append(PackageStr)
				filename_input2 =filename_input.split(".")
				filename_input2str = ""
				count = 0
				for x in filename_input2:
					count = count +1
					if count == len(filename_input2)-1:
						 continue 
					if count == len(filename_input2): 
						filename_input2str = filename_input2str +x
					else:
						filename_input2str = filename_input2str +x+"."
				Instanz.insert_line(filename_input,output_path, 0, "@startuml")
				Instanz.insert_line(filename_input,output_path,Instanz.number_of_lines(filename_input,output_path),"\n"+"}"+ "\n"+"}"+"\n"+ "@enduml")
				Instanz.insert_line(filename_input,output_path, 1,"\n"+"\n"+"\n"+"\n"+ Instanz.ClassName(filename_input,Package)+"\n") 
				filename_input2 =  filename_input2str
				filename_package = DataCheck.set_ModelsinPackages(filename_input2, output_path)
				for i in range(0,len(filename_package)-1,1):
					filename_output = DataCheck.setUMLModell(filename_package[i], output_path)
					Instanz.set_Attribute_public(filename_package[i],filename_output, output_path,parameter,variables,primitivevariables,complexvariables)			
					Instanz.set_Attribute_protected(filename_package[i], filename_output,output_path,parameter,variables,primitivevariables,complexvariables)
					Instanz.set_initialMethode(filename_package[i],filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
					Instanz.set_Methode(filename_package[i], filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
					Instanz.insert_line(filename_package[i],output_path, 0, "@startuml")
					Instanz.insert_line(filename_package[i],output_path,Instanz.number_of_lines(filename_package[i],output_path)+1,"\n"+"}"+ "\n"+"}"+"\n"+ "@enduml")
					Instanz.insert_line(filename_package[i],output_path, 1,"\n"+"\n"+ Instanz.ClassName(filename_package[i],Package)+"\n") 
		return filename_input
Instanz = ClassDiagram()
if __name__ == "__main__":
	Instanz = ClassDiagram()
  
