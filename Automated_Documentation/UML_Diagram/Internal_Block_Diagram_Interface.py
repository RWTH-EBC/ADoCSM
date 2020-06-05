from UML_Diagram import General
from UML_Diagram import Object_Oriented_Relations
from UML_Diagram import ClassDiagram
from UML_Diagram import UML_Interface
import os
import shutil
import numpy as np

ClassConverter = General.Class_Converter()
Realtion =  Object_Oriented_Relations.Relation()
DataCheck = General.DataCheck
ClassDiagram = ClassDiagram.ClassDiagram()
UML_Interface = UML_Interface.UMLClassDiagram_MainInterface()

### Visualise a Internal_Block_Diagram

class Internal_Block_Diagram_Interface():
    
    def Internal_Block_Diagram(self,filename_input,output_path,AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation,showconstant,showType):
        fileList = os.listdir(output_path)
        Package = []
        for f in fileList:
            f=output_path+"\\"+f
            if os.path.isfile(f):
                os.remove(f)
        DataCheck.AixLibPath_exist(AixLib_path)
        
        DataCheck.filename_exist(filename_input)
        RelationModel = filename_input.split("\\")
        RelationModel = RelationModel[len(RelationModel)-1].replace(".mo","")
        #RelationModel = "MassFlowRateChoke"
        
        filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) 
        
        #Instanz.getRelationExample(filename_input, AixLib_path)
        Instanz.put_full_Package(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package)
        for z in Realtion.setConnectinModel(filename_input, AixLib_path):
            ClassDiagram.insert_line(filename_input,output_path,ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z+"\n" )
        classname = Internal_Block_Diagram_Interface.packagename(self, filename_input)
        if Instanz.packagename(filename_input)!=None:
            ClassDiagram.insert_line(filename_input,output_path, 0, "@startuml")
            ClassDiagram.insert_line(filename_input,output_path,ClassDiagram.number_of_lines(filename_input,output_path),"\n"+"}"+ "\n"+ "@enduml")
            ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+"\n"+"\n"+"\n"+ classname+"\n")    
       
        for i in Realtion.get_Relation(filename_input,AixLib_path,block):
            
            i= i.split(",")
            filename_input = i[0] 
            RelationModel = i[1]
            filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path) #Formats the file and outputs the file
            DataCheck.filename_exist(filename_input)
            ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
            
        DataCheck.Appender(output_path, finalData)
        """ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
        for z in Realtion.setConnectinModel(filename_input, AixLib_path):
               ClassDiagram.insert_line(filename_input,output_path,ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z+"\n" )
        for i in Realtion.get_Relation(filename_input,AixLib_path,block):
            Package = []
            i= i.split(",")
            if len(i)==3:
                filename_input = i[0] 
                RelationModel = i[1]
                Package.append(i[2])
                
            else:
                filename_input = i[0] 
                RelationModel = i[1]
            
            DataCheck.filename_exist(filename_input)
            filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)   
            T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
            continue"""
            
    def packagename(self,filename_input):  
        self.readfile_in = open(filename_input,'r')
        stereotyp=[]
        for line in self.readfile_in.readlines():
            x = line.split()
            x_array = np.asarray(x)
            if len(x_array)>0:    
                if x_array[0] == 'function':
                    stereotyp.append(x_array)
                    classname = " package "+stereotyp[0][1] + " << " +stereotyp[0][0] + " >>  {"
                    return classname
                if x_array[0] == 'partial' and x_array[1]=="connector":
                    stereotyp.append(x_array)
                    classname= " package "+stereotyp[0][2] + " << " +stereotyp[0][0] +" "+ stereotyp[0][1]+ " >>  {"
                    return classname
                if x_array[0] == 'partial':
                    stereotyp.append(x_array)
                    classname= " package "+stereotyp[0][2] + " << " +stereotyp[0][0]+ " >>  {"
                    return classname
                if x_array[0] == "model":
                    stereotyp.append(x_array)
                    classname = "package "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
                    return classname
                if x_array[0] == "block":
                    stereotyp.append(x_array)
                    classname = "package "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
                    return classname
                if x_array[0] == "connector":
                    stereotyp.append(x_array)
                    classname = "package "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
                    return classname
                if x_array[0] == "type":
                    stereotyp.append(x_array)
                    classname = "package "+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >> {" 
                    return classname
                if x_array[0] == "record":
                    stereotyp.append(x_array)
                    classname = "package"+stereotyp[0][1] + " << " +stereotyp[0][0]+ " >>  {"
                    return classname  
                    
                    
    def put_full_Package(self,filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package):
        filename_output = DataCheck.setUMLModell(filename_input, output_path)
        ClassDiagram.set_Attribute_public(filename_input,filename_output, output_path,parameter,variables,primitivevariables,complexvariables,Relation,showconstant)            
        ClassDiagram.set_Attribute_protected(filename_input, filename_output,output_path,parameter,variables,primitivevariables,complexvariables,showconstant)
        ClassDiagram.set_initialMethode(filename_input,filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
        ClassDiagram.set_Methode(filename_input, filename_output,output_path,parameter,variables,primitivevariables,complexvariables,methode)
        return filename_input
    
    def getRelationExample(self, filename_input, AixLib_path):
        self.ListLibrary = DataCheck.allModelicaLibrary(AixLib_path)
        self.filename_input = filename_input
        readfile_in = open(self.filename_input, 'r+')
        ListRelation = []
        ModelList = []
        for z in Realtion.setConnectinModel(filename_input, AixLib_path):
            w = z.split('"')
            x =  z.split(':')
            x = x[0].split('"')
            ModelList.append(w[0])
            ModelList.append(x[len(x)-1])
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
        for z in ModelList:
            z = z.lstrip()
            RelationModel = z
            
            relation_directory = DataCheck.set_relationmodel_path(AixLib_path, RelationModel, OriginalLibrary)

         
    def setdirection(self,finalData):
        readfile_in = open(finalData,"r+")
        for line in readfile_in.readflines():
            print(line)
        
   
                 
                    
                    
Instanz = Internal_Block_Diagram_Interface()


if __name__ == "__main__":
    filename_input= r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\Actuators\Valves\ExpansionValves\Examples\MassFlowRateChoke.mo"
    AixLib_path=r"C:\Users\hinack\Dropbox\09_Modelica_Library"
    output_path =  r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
    Model = [filename_input]
    finalData = r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil.java"
    parameter = True    
    variables = False
    Relation = False
    Medium = False
    primitivevariables= False
    methode = False
    complexvariables = False
    HierarchyLevel = 10
    block =   True  
    showPackages = True 
    showconstant = False
    showType = True
    showConnect = True
    Instanz.Internal_Block_Diagram(filename_input, output_path, AixLib_path, HierarchyLevel, parameter, variables, primitivevariables, complexvariables, methode, block, showPackages, Relation, showconstant, showType)
    UML_Interface.test(finalData,0,"@startuml{")    
    UML_Interface.test(finalData,UML_Interface.test2(finalData), " \n @enduml") 
    
    
    
    print("Conversion Succsesfull!")
                    
                    