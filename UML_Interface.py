from UML_Diagram import General
from UML_Diagram import Object_Oriented_Relations
from UML_Diagram import ClassDiagram
import os
import shutil

ClassConverter = General.Class_Converter()
Realtion =  Object_Oriented_Relations.Relation()
DataCheck = General.DataCheck
ClassDiagram = ClassDiagram.ClassDiagram()


 
class UMLClassDiagram_MainInterface():
    
    
    
    def Class_Interface(self,filename_input,output_path,AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation):
        
        fileList = os.listdir(output_path)
        for f in fileList:
            f=output_path+"\\"+f
            if os.path.isfile(f):
                os.remove(f)
        DataCheck.AixLibPath_exist(AixLib_path)
        DataCheck.filename_exist(filename_input)
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
        RelationModel = filename_input
        filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
        ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)
       
        if HierarchyLevel > 0 :
            for z in Realtion.set_Relation(filename_input, AixLib_path):
             
                DataCheck.filename_exist(filename_input)
                ClassDiagram.insert_line(filename_input,output_path,ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z+"\n" )
                if HierarchyLevel > 1:
                    for i in Realtion.get_Relation(filename_input,AixLib_path,block):
                        i= i.split(",")
                        filename_input = i[0] 
                        RelationModel = i[1]
                        filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                        ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)
                        Model1.append(filename_input)
                        for z in Realtion.set_Relation(filename_input, AixLib_path):
                            ClassDiagram.insert_line(filename_input,output_path,ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z+"\n" )
        if HierarchyLevel >2 :
            for w in range(0,len(Model1),1):
                for i in Realtion.get_Relation(Model1[w],AixLib_path,block):
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
                   
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        
                        Model2.append(T[i])
                        Model21.append(T[i])
                    Model2.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z+"\n" )
            for x in range(0,len(Model21),1):
                    for z in Realtion.set_Relation(Model21[x], AixLib_path):
                        ClassDiagram.insert_line(Model21[x],output_path, ClassDiagram.number_of_lines(Model21[x],output_path)-1,"\n"+z +"\n")
       
        if HierarchyLevel >3:
            for w in range(0,len(Model2),1):
                for i in Realtion.get_Relation(Model2[w],AixLib_path,block):
                    
                    
                    Package = []
                    i= i.split(",")
                    #print(i)
                    if len(i)==3:
                        filename_input = i[0] 
                        RelationModel = i[1]
                        Package.append(i[2])
                    else:
                        filename_input = i[0] 
                        RelationModel = i[1]
                    DataCheck.filename_exist(filename_input)
                    filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)  
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model31.append(T[i])
                        Model3.append(T[i])
                        continue
                    Model3.append(filename_input)
                    #print(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z +"\n")
                        continue
                
                ##Package   
                for x in range(0,len(Model31),1):
                    for z in Realtion.set_Relation(Model31[x], AixLib_path):
                        ClassDiagram.insert_line(Model31[x],output_path, ClassDiagram.number_of_lines(Model31[x],output_path)-1,"\n"+z +"\n")
        #print(Model3)
        if HierarchyLevel >4 :
            for w in range(0,len(Model3),1):
                for i in Realtion.get_Relation(Model3[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model41.append(T[i])
                        Model4.append(T[i])
                        continue
                    Model4.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z +"\n")
                        continue
                for x in range(0,len(Model41),1):
                    for z in Realtion.set_Relation(Model41[x], AixLib_path):
                        ClassDiagram.insert_line(Model41[x],output_path, ClassDiagram.number_of_lines(Model41[x],output_path)-1,"\n"+z +"\n")
        if HierarchyLevel >5 :
            for w in range(0,len(Model4),1):
                for i in Realtion.get_Relation(Model4[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model51.append(T[i])
                        Model5.append(T[i])
                        continue
                    Model5.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z +"\n")
            for x in range(0,len(Model51),1):
                    for z in Realtion.set_Relation(Model51[x], AixLib_path):
                        ClassDiagram.insert_line(Model51[x],output_path, ClassDiagram.number_of_lines(Model51[x],output_path)-1,"\n"+z +"\n")
        if HierarchyLevel >6 :
            for w in range(0,len(Model5),1):
                for i in Realtion.get_Relation(Model5[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model61.append(T[i])
                        Model6.append(T[i])
                        continue
                    
                    Model6.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
                for x in range(0,len(Model61),1):
                    for z in Realtion.set_Relation(Model61[x], AixLib_path):
                        ClassDiagram.insert_line(Model61[x],output_path, ClassDiagram.number_of_lines(Model61[x],output_path)-1,"\n"+z +"\n")
        if HierarchyLevel >7 :
            for w in range(0,len(Model6),1):
                for i in Realtion.get_Relation(Model6[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model71.append(T[i])
                        Model7.append(T[i])
                        continue
                    Model7.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
                for x in range(0,len(Model71),1):
                    for z in Realtion.set_Relation(Model71[x], AixLib_path):
                        ClassDiagram.insert_line(Model71[x],output_path, ClassDiagram.number_of_lines(Model71[x],output_path)-1,"\n"+z +"\n")
        
        if HierarchyLevel >8 :
            for w in range(0,len(Model7),1):
                for i in Realtion.get_Relation(Model7[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model81.append(T[i])
                        Model8.append(T[i])
                        continue
                    Model8.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
            for x in range(0,len(Model81),1):
                    for z in Realtion.set_Relation(Model81[x], AixLib_path):
                        ClassDiagram.insert_line(Model81[x],output_path, ClassDiagram.number_of_lines(Model81[x],output_path)-1,"\n"+z +"\n")
        
        if HierarchyLevel >9 :
            for w in range(0,len( Model8),1):
                for i in Realtion.get_Relation(Model8[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model91.append(T[i])
                        Model9.append(T[i])
                        continue
                    
                    Model9.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
        for x in range(0,len(Model91),1):
                    for z in Realtion.set_Relation(Model91[x], AixLib_path):
                        ClassDiagram.insert_line(Model91[x],output_path, ClassDiagram.number_of_lines(Model91[x],output_path)-1,"\n"+z +"\n")
        if HierarchyLevel >10 :
            for w in range(0,len(Model9),1):
                for i in Realtion.get_Relation(Model9[w],AixLib_path,block):
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
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model10.append(T[i])
                        Model11.append(T[i])
                        continue
                    Model10.append(filename_input)
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                        ClassDiagram.insert_line(filename_input,output_path, 1,"\n"+z +"\n")
            for x in range(0,len(Model11),1):
                for z in Realtion.set_Relation(Model11[x], AixLib_path):
                    ClassDiagram.insert_line(Model11[x],output_path, ClassDiagram.number_of_lines(Model11[x],output_path)-1,"\n"+z +"\n")
    def test(self,filename_output,insert_pos,line):
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
    def sort(self,finalData):
        readfile_in = open(finalData,"r")
        
        readfile_out = open(r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil2.java","w")
        RelationList = []
        for line in readfile_in.readlines():
            if line.find("<|--")>-1 or line.find("*--")>-1 or line.find("<|..")>-1 or line.find("@enduml")>-1:
                RelationList.append(line)#
                #print(line)
            else:
                readfile_out.writelines(line)
        for w in RelationList:
            
            readfile_out.writelines("\n"+w+"\n")
            
  
#filename_input= r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves\IsenthalpicExpansionValve.mo"#filename_input =     r"C:\users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\BoilerCHP\Boiler.mo"
#filename_input=r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\HeatExchangers\ConstantEffectiveness.mo"
#filename_input = r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\BoilerCHP\Boiler.mo"   
#filename_input = r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\HeatPumps\Calibration\ScrollWaterToWater.mo"
filename_input=r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\FixedResistances\Junction.mo"
filename_output= r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
AixLib_path=r"C:\Users\hinack\Dropbox\09_Modelica_Library"
output_path =  r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
Model = [filename_input]
finalData = r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil.java"
parameter = False
variables = False
Relation = False
Medium = False
primitivevariables= False
methode = False
complexvariables = False
HierarchyLevel = 10
block = False
showPackages = False 


if __name__ == "__main__":
    print("start")    
    
    #for filename in os.listdir(filename_output):
     #   os.remove(filename)
    Instanz = UMLClassDiagram_MainInterface()
    Instanz.Class_Interface(filename_input, output_path, AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation)  
    DataCheck.Appender(output_path, finalData)
    
    Instanz.test(finalData,0,"@startuml{")    
    Instanz.test(finalData,Instanz.test2(finalData), " \n @enduml")  
    Instanz.sort(finalData)
    #t= output_path+"\\"+"TempData"
    #shutil.rmtree(t)
    
    print("Conversion Erfolgreich!")
     
     
 
 
 
    
    

