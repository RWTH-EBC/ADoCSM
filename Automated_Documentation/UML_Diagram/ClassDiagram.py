
import linecache
import numpy as np


from UML_Diagram import General
#from UML_Diagram import Object_Oriented_Relations


DataCheck = General.DataCheck
Class_Converter = General.Class_Converter
class ClassDiagram():
    
    
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
        array0 = []
        array01 = []
        array1 = []
        array12 = []
        array2 = []
        array21 = []
        array3 = []
        array31 = []
        array4 = []
        array41 = []
        array5 = []
        array6 = []
        array06= []
        array07= []
        array08 = []
        array09 = []
        array10 = []
        Counter_InitialEquation = []
        Countlistfor = []
        Countlistif = []
        Countlistelseif = []
        Countlistelse = []
        countlistendif = []
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
                x = line.split()         
                x_array = np.asarray(x)
                if len(x_array)>0:
                    if methode ==True:
                        #############################################################################
                        ## if
                        if x_array[0] == "if" and len(countlistendif)==0:
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array1.append(line[:x-1])
                            array01.append(x_array)
                            Countlistif.append(count)
                            pass
                    
                    if methode ==True:
                        if len(Countlistif)%2==1 and len(Countlistelseif)==0 and x_array[0] != "if" and  x_array[0] != "elseif"and  x_array[0] != "else" and  x_array[1] != "if;":
                            line = line.replace("\n"," ")
                            x = line.find('"')
                           
                            array1.append(line[:x-1])    
                            array06.append(x_array)
                    
                    if methode ==True:
                        #############################################################################
                        ## elseif
                        if x_array[0]=="elseif":
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array6.append(line[:x-1])    
                            Countlistelseif = []
                            Countlistelseif.append(count)
                            countlistendif.append(count)
                            array1str =""
                            if len(array1)>1:
                                for i in array1:
                                    array1str=array1str+(i)+";"
                                    continue
                                readfile_out.write("\n # "+"("+array1str+")")
                                countlistendif = []
                            if len(array1)==1:
                                readfile_out.write("\n # "+"("+array1[0]+")")
                                countlistendif = []
                          
                            if len(array6)>1:
                                for w in range(0,len(array6),1):
                                    readfile_out.write("\n # "+"("+array6[w]+")")
                                   
                                    continue
                                countlistendif = []
                                Countlistelseif = []
                                array6=[]
                            array1 = []
                           
                    if methode ==True:
                        if len(array6)==1:
                            readfile_out.write("\n # "+"("+array6[0]+")")
                            array6 = []
                            continue
                    
                    if methode ==True:
                        if len(Countlistif)%2==1 and len(Countlistelseif)%2==1 and  x_array[0] != "elseif" and len(countlistendif)<2:
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array6.append(line[:x-1])    
                            array06.append(x_array)
                            array1str =""
                            if len(array6)>0:
                                for i in array6:
                                    array1str=array1str+(i)+";"
                                readfile_out.write(" ("+array1str+")")
                            Countlistelseif = [1]
                            array6 = []
                    
                    #############################################################################
                    ## else
                    if methode ==True:
                        if x_array[0] == "else":
                            line = line.replace("\n"," ")
                            x = line.find('"') 
                            if line.find("assert")>-1:
                                x = line.find(';')
                            array2.append(line[:x-1])
                            Countlistelse.append(count)
                            continue
                            pass
                    if methode ==True:
                        if len(Countlistif)%2==1 and len(Countlistelse)%2==1 and x_array[0] != "if" and  x_array[0] != "elseif" and x_array[0] != "end" and x_array[0] != "else":
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array2.append(line[:x-1])    
                            array06.append(x_array)
                            continue
                            pass
                    #############################################################################
                    ## end if
                    if methode ==True:
                        if x_array[0] == "end" and x_array[1] == "if"  :
                            countlistendif.append(count)
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            if len(Countlistelseif)==0:
                                array1str =""
                                for i in array1:
                                     array1str = array1str+i+" "
                                readfile_out.write("\n # "+"("+array1str+")") 
                                continue
                            array5.append(line[:x-1])
                            Countlistif.append(count)
                            Countlistelseif.append(count)
                            array1str =""
                            if len(array2)>0:
                                for i in array2:
                                    array1str=array1str+(i)+";"
                                readfile_out.write("\n # "+"("+array1str+")")
                            if len(countlistendif)%2==1:
                                readfile_out.write("\n # " +"("+array5[0]+")")
                           
                            array5 = []
                            array2 = []
                            countlistendif = []
                            continue
                    
                    #############################################################################
                    ## for       
                    if methode ==True:
                            if x_array[0] == "for" and len(Countlistif)%2==0:
                                line = line.replace("\n"," ")
                                array08.append(line)
                                Countlistfor.append(count)
                    if methode ==True:
                            if len(Countlistfor)%2 == 1 and x_array[0] != "for" and x_array[0] != "end"and  len(Countlistif)%2==0 :
                                line = line.replace("\n"," ")
                                array08.append(line)
                    
                    #############################################################################
                    ## end for       
                    if methode ==True:
                            if x_array[0] == "end" and x_array[1] =="for" and len(Countlistif)%2==0:
                                Countlistfor = []
                                line = line.replace("\n"," ")
                                array08.append(line)
                                array08str =""
                                for i in array08:
                                    array08str=array08str+(i)
                                readfile_out.write("\n # "+"("+array08str+")")
                                array08 = []
                if methode ==True:
                    if len(x_array)>0  and len(Countlistfor)%2 == 0 and len(Countlistif)%2==0 :
                        if x_array[0] == "annotation":
                            break
                        if methode ==True:
                            if line[0:7] == "connect":
                                model1 = line[line.find("(")+1:line.find(",")]
                                model2 =line [line.find(",")+1:line.find(")")]
                                str = model1  +" #.. "+ model2
                                array3.append(str)
                                pass
                        if methode ==True:
                            if len(x_array)>1:
                                if x_array[1] == "=" or line.find("=") > -1:
                                    array4.append(line)
                                    pass
                        if methode ==True:
                            if x_array[0] =="assert":
                                array07.append(line)
                        continue
                    pass
        #assert
        ################################################################################################################################
        i = 0
        while i<len(array07):
            a = array07[i].find('annotation')
            x = array07[i].find(')')
            readfile_out.write(("\n # "+ array07[i][0:x+1]))
            i = i+1
        ## =
        ##############################################################################################################################
        i=0
        while i<len(array4):
            array4[i] = array4[i].replace(" ( ","(")
            array4[i] = array4[i].replace(" ) ",")")
            array4[i] = array4[i].replace(" = ","=")
            z = array4[i].find("=")
            y = array4[i].find('"')
            w = array4[i].find(';')
            x = array4[i][z+1:y-1]
            q = array4[i][z+1:w-1]
            
            if y > -1:
               readfile_out.write(("\n # "+ array4[i][0:z] +" (" + x  +")"))
            else:
                readfile_out.write(("\n + "+ array4[i][0:z] +" (" + q  +")"))
            i = i+1
            pass
        ##if
        """"i=0
        while i<len(array1):
            array1[i] = array1[i].replace(" = ","=")
            y = array1[i].find('"')  
            x = array1[i].find("then")
            z = array1[i].find("(")
            w = array1[i].find(")")
            if array01[i][2] == "then":
                readfile_out.write(("\n + "+ array01[i][0]+" "+array01[i][1]+" "+array01[i][2]+" ("+array1[i][x+4:y])+")")
            else:
                readfile_out.write(("\n + "+ array01[i][0]+" "+array1[i][z:y]))
            i = i+1
            pass"""
        """##elseif
        i=0
        while i<len(array6):
            array6[i] = array6[i].replace(" = ","=")
            y = array6[i].find('"')  
            x = array6[i].find("then")
            z = array6[i].find("(")
            w = array6[i].find(")")
            readfile_out.write("\n + "+array06[i][0]+" "+array6[i][z:y] )
            i=i+1
            pass
        
        ##else
        i=0
        while i<len(array2):
            y = array2[i].find('"')  
            x = array2[i].find(')')  
            readfile_out.write(("\n + "+ array2[i][0:x+1]))
            i = i+1
            pass
      ##end if
        i=0
        while i<len(array5):
            readfile_out.write(("\n + "+ array5[i][0]+" "+array5[i][1][0:2])+"()")
            i = i+1
            pass
        ##for
        #####################################################################################################
        i=0
        while i<len(array08):
            readfile_out.write(("\n + "+ array08[i]))
            i = i+1
            pass"""
       
       
        
        self.readfile_in.close()
        readfile_out.close()
    
    ################################################################################################################################################################################################
    #Searches and Writes Methods in PlantUML Format   
    def set_Methode(self,filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode):
        self.readfile_in = open(filename_input,'r')
        readfile_out = open(filename_output,"a")
        array0 = []
        array01 = []
        array1 = []
        array12 = []
        array2 = []
        array21 = []
        array3 = []
        array31 = []
        array4 = []
        array41 = []
        array5 = []
        array6 = []
        array06= []
        array07= []
        array08 = []
        array09 = []
       
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
                x = line.split()         
                x_array = np.asarray(x)
                if len(x_array)>0:
                    if methode ==True:
                        #############################################################################
                        ## if
                        if x_array[0] == "if" and len(countlistendif)==0:
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array1.append(line[:x-1])
                            array01.append(x_array)
                            Countlistif.append(count)
                            pass
                    
                    if methode ==True:
                        if len(Countlistif)%2==1 and len(Countlistelseif)==0 and x_array[0] != "if" and  x_array[0] != "elseif"and  x_array[0] != "else" and  x_array[1] != "if;":
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array1.append(line[:x-1])    
                            array06.append(x_array)
                    
                    if methode ==True:
                        #############################################################################
                        ## elseif
                        if x_array[0]=="elseif":
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array6.append(line[:x-1])    
                            Countlistelseif = []
                            Countlistelseif.append(count)
                            countlistendif.append(count)
                            array1str =""
                            if len(array1)>1:
                                for i in array1:
                                    array1str=array1str+(i)+";"
                                    continue
                                readfile_out.write("\n + "+"("+array1str+")")
                                countlistendif = []
                            if len(array1)==1:
                                readfile_out.write("\n + "+"("+array1[0]+")")
                                countlistendif = []
                            if len(array6)>1:
                                for w in range(0,len(array6),1):
                                    readfile_out.write("\n + "+"("+array6[w]+")")
                                    continue
                                countlistendif = []
                                Countlistelseif = []
                                array6=[]
                            array1 = []
                           
                    if methode ==True:
                        if len(array6)==1:
                                readfile_out.write("\n + "+"("+array6[0]+")")
                                array6 = []
                                continue
                    
                    if methode ==True:
                        if len(Countlistif)%2==1 and len(Countlistelseif)%2==1 and  x_array[0] != "elseif" and len(countlistendif)<2:
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array6.append(line[:x-1])    
                            array06.append(x_array)
                            array1str =""
                            if len(array6)>0:
                                for i in array6:
                                    array1str=array1str+(i)+";"
                                readfile_out.write(" ("+array1str+")")
                            Countlistelseif = [1]
                            array6 = []
                  
                    if methode ==True:
                        if x_array[0] == "else":
                            line = line.replace("\n"," ")
                            x = line.find('"') 
                            if line.find("assert")>-1:
                                x = line.find(';')
                            array2.append(line[:x-1])
                            Countlistelse.append(count)
                            continue
                            pass
                    if methode ==True:
                        if len(Countlistif)%2==1 and len(Countlistelse)%2==1 and x_array[0] != "if" and  x_array[0] != "elseif" and x_array[0] != "end" and x_array[0] != "else":
                            
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            array2.append(line[:x-1])    
                            array06.append(x_array)
                            continue
                            pass
                    
                    #############################################################################
                    ## end for
                    if methode ==True:
                        if x_array[0] == "end" and x_array[1] == "if":
                            countlistendif.append(count)
                            line = line.replace("\n"," ")
                            x = line.find('"')
                            if len(Countlistelseif)==0:
                                array1str =""
                                for i in array1:
                                     array1str = array1str+i+" "
                                readfile_out.write("\n + "+"("+array1str+")") 
                            array5.append(line[:x-1])
                            Countlistif.append(count)
                            Countlistelseif.append(count)
                            array1str =""
                            if len(array2)>0:
                                for i in array2:
                                    array1str=array1str+(i)+";"
                                readfile_out.write("\n + "+"("+array1str+")")
                            readfile_out.write("\n + " +"("+array5[0]+")")
                            array2 = []
                            countlistendif = []
                    if methode ==True:
                            if x_array[0] == "for" and len(Countlistif)%2==0:
                                line = line.replace("\n"," ")
                                array08.append(line)
                                Countlistfor.append(count)
                    if methode ==True:
                            if len(Countlistfor)%2 == 1 and x_array[0] != "for" and x_array[0] != "end"and  len(Countlistif)%2==0 :
                                line = line.replace("\n"," ")
                                array08.append(line)
                    if methode ==True:
                            if x_array[0] == "end" and x_array[1] =="for" and len(Countlistif)%2==0:
                                Countlistfor = []
                                line = line.replace("\n"," ")
                                array08.append(line)
                                array08str =""
                                for i in array08:
                                    array08str=array08str+(i)
                                readfile_out.write("\n + "+"("+array08str+")")
                                array08 = []
                if methode ==True:
                    if len(x_array)>0  and len(Countlistfor)%2 == 0 and len(Countlistif)%2==0 :
                        if x_array[0] == "annotation":
                            break
                        if methode ==True:
                            if line[0:7] == "connect":
                                model1 = line[line.find("(")+1:line.find(",")]
                                model2 =line [line.find(",")+1:line.find(")")]
                                str = model1  +" #.. "+ model2
                                array3.append(str)
                                pass
                        if methode ==True:
                            if len(x_array)>1:
                                if x_array[1] == "=" or line.find("=") > -1:
                                    array4.append(line)
                                    pass
                        if methode ==True:
                            if x_array[0] =="assert":
                                array07.append(line)
                        continue
                    pass
        #assert
        ################################################################################################################################
        i = 0
        while i<len(array07):
            a = array07[i].find('annotation')
            x = array07[i].find(')')
            readfile_out.write(("\n + "+ array07[i][0:x+1]))
            i = i+1
        ## =
        ##############################################################################################################################
        i=0
        while i<len(array4):
            array4[i] = array4[i].replace(" ( ","(")
            array4[i] = array4[i].replace(" ) ",")")
            array4[i] = array4[i].replace(" = ","=")
            z = array4[i].find("=")
            y = array4[i].find('"')
            w = array4[i].find(';')
            x = array4[i][z+1:y-1]
            q = array4[i][z+1:w-1]
            
            if y > -1:
               readfile_out.write(("\n + "+ array4[i][0:z] +" (" + x  +")"))
            else:
                readfile_out.write(("\n + "+ array4[i][0:z] +" (" + q  +")"))
            i = i+1
            pass
        ##if
        """"i=0
        while i<len(array1):
            array1[i] = array1[i].replace(" = ","=")
            y = array1[i].find('"')  
            x = array1[i].find("then")
            z = array1[i].find("(")
            w = array1[i].find(")")
            if array01[i][2] == "then":
                readfile_out.write(("\n + "+ array01[i][0]+" "+array01[i][1]+" "+array01[i][2]+" ("+array1[i][x+4:y])+")")
            else:
                readfile_out.write(("\n + "+ array01[i][0]+" "+array1[i][z:y]))
            i = i+1
            pass"""
        """##elseif
        i=0
        while i<len(array6):
            array6[i] = array6[i].replace(" = ","=")
            y = array6[i].find('"')  
            x = array6[i].find("then")
            z = array6[i].find("(")
            w = array6[i].find(")")
            readfile_out.write("\n + "+array06[i][0]+" "+array6[i][z:y] )
            i=i+1
            pass
        
        ##else
        i=0
        while i<len(array2):
            y = array2[i].find('"')  
            x = array2[i].find(')')  
            readfile_out.write(("\n + "+ array2[i][0:x+1]))
            i = i+1
            pass
      ##end if
        i=0
        while i<len(array5):
            readfile_out.write(("\n + "+ array5[i][0]+" "+array5[i][1][0:2])+"()")
            i = i+1
            pass
        ##for
        #####################################################################################################
        i=0
        while i<len(array08):
            readfile_out.write(("\n + "+ array08[i]))
            i = i+1
            pass"""
        self.readfile_in.close()
        readfile_out.close()
        return Counter_Equation 
       
    
    
    
    
    def insert_line(self,filename_input, output_path,insert_pos, line):
        filename_output = DataCheck.setUMLModell(filename_input, output_path)
        f = open(filename_output,"r+")
        lines = f.readlines()
        f.close()
        lines.insert(insert_pos, line)
        f = open(filename_output, 'w')
        f.writelines(lines)
        f.close()
        return filename_output
       
     
    def number_of_lines(self,filename_input,output_path):
        self.filename = DataCheck.setUMLModell(filename_input, output_path)
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
                            classname = "enum     "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {\n" +line[x:y]+"\n"+line[y:z]+"\n"+line[z:w]
                        else:
                            classname = "enum     "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >> {" 
                        return classname
                    if x_array[0] == "record":
                        stereotyp.append(x_array)
                        classname = "class     "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
                        return classname
            
            ##for Replaceable Packages or Models
            if len(Package)>0:
                if len(x_array)>0:
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
                        classname = "enum     "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {\n" +line[x:y]+"\n"+line[y:z]+"\n"+line[z:w]
                        return classname
                    if x_array[0] == "record":
                        stereotyp.append(x_array)
                        classname ="package "+ Package[0] +"{\n"+ "class     "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
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
        filename_output = DataCheck.setUMLModell(filename_input, output_path)
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
                    filename_package = DataCheck.set_ModelsinPackages(filename_input2, output_path)
                    if filename_input in filename_package:
                        filename_package.remove(filename_input)
                    for i in range(0,len(filename_package)-1,1):
                        filename_output = DataCheck.setUMLModell(filename_package[i], output_path)
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
        filename_output = DataCheck.setUMLModell(filename_input, output_path)
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
  
