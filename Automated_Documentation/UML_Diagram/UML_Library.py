#Zuerst Package erkennen uhnd auflisten
#DAnn Relation und ganzen Attribute8#
#In GUI einbauen
#packages in packages noch beachten
from UML_Diagram import General
from UML_Diagram import Object_Oriented_Relations
from UML_Diagram import ClassDiagram
from UML_Diagram import UML_Interface
import os
import shutil

ClassConverter = General.Class_Converter()
Realtion =  Object_Oriented_Relations.Relation()
DataCheck = General.DataCheck
ClassDiagram = ClassDiagram.ClassDiagram()
UML_Interface = UML_Interface.UMLClassDiagram_MainInterface()



class UMLLibraryClassDiagram():
    
    def Library_Interface(self,filename_input,output_path,AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation,showconstant,showType):
        Package = []
        Model1 = []
        Model2 = []
        Model3 = []
        Model4 = []
        Model5 = []
        Model21 = []
        fileList = os.listdir(output_path)
        for f in fileList:
            f=output_path+"\\"+f
            if os.path.isfile(f):
                os.remove(f)
        if HierarchyLevel>0:
            RelationModel = filename_input.split(".")
            RelationModel = RelationModel[0].split("\\")
            RelationModel = RelationModel[len(RelationModel)-1]
            DataCheck.AixLibPath_exist(AixLib_path)
            T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
            S = DataCheck.getPackagesinPackages(T , output_path)
            S = (S[0].split("\\"))
            PackageName = S[len(S)-1].split(".")
            count = 0
            xstr = ""
            for x in PackageName[:-2]:
                if count == 0:
                    xstr =  xstr+x 
                else:
                    xstr = xstr +"."+x
                count = count +1 
            Package.append(xstr)
            PackageList = DataCheck.set_ModelsinPackages(T , output_path)
            for i in range(0,len(PackageList),1):
                DataCheck.filename_exist(PackageList[i])
                ClassDiagram.put_full_class(PackageList[i],output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
                Model1.append(PackageList[i])
                continue
        if HierarchyLevel>1:
            for w in range(0,len(Model1),1):
                for i in Realtion.get_Relation(Model1[w],AixLib_path,block):
                    PackageList = []
                    Package = []
                    i= i.split(",")
                    if len(i)==3:
                        filename_input = i[0] 
                        RelationModel = i[1]
                        Package.append(i[2])
                    else:
                        filename_input = i[0] 
                        RelationModel = i[1]
                   
                    RelationModel = filename_input.split(".")
                    RelationModel = RelationModel[0].split("\\")
                    RelationModel = RelationModel[len(RelationModel)-1]
                   
                    T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                    
                 
                    S = DataCheck.getPackagesinPackages(T , output_path)
                   
                    S = (S[0].split("\\"))
                    PackageName = S[len(S)-1].split(".")
                    count = 0
                    xstr = ""
                    for x in PackageName[:-2]:
                        if count == 0:
                            xstr =  xstr+x 
                        else:
                            xstr = xstr +"."+x
                        count = count +1 
                    Package.append(xstr)
                    PackageList = DataCheck.set_ModelsinPackages(T , output_path)
                    
                    for i in range(0,len(PackageList),1):
                        DataCheck.filename_exist(PackageList[i])
                        ClassDiagram.put_full_class(PackageList[i],output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
                        Model2.append(PackageList[i])
                        if Relation == True:
                            for z in Realtion.set_Relation(PackageList[i], AixLib_path):
                                ClassDiagram.insert_line(PackageList[i],output_path,ClassDiagram.number_of_lines(PackageList[i],output_path)-1,"\n"+z+"\n" )
                                continue
            
        if HierarchyLevel>2:
            for w in range(0,len(Model2),1):
                for i in Realtion.get_Relation(Model2[w],AixLib_path,block):
                    PackageList = []
                    Package = []
                    i= i.split(",")
                    if len(i)==3:
                        filename_input = i[0] 
                        RelationModel = i[1]
                        Package.append(i[2])
                    else:
                        filename_input = i[0] 
                        RelationModel = i[1]
                   
                    RelationModel = filename_input.split(".")
                    RelationModel = RelationModel[0].split("\\")
                    RelationModel = RelationModel[len(RelationModel)-1]
                   
                    T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                    
                 
                    S = DataCheck.getPackagesinPackages(T , output_path)
                   
                    S = (S[0].split("\\"))
                    PackageName = S[len(S)-1].split(".")
                    count = 0
                    xstr = ""
                    for x in PackageName[:-2]:
                        if count == 0:
                            xstr =  xstr+x 
                        else:
                            xstr = xstr +"."+x
                        count = count +1 
                    Package.append(xstr)
                    PackageList = DataCheck.set_ModelsinPackages(T , output_path)
                    
                    for i in range(0,len(PackageList),1):
                        DataCheck.filename_exist(PackageList[i])
                        ClassDiagram.put_full_class(PackageList[i],output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
                        Model3.append(PackageList[i])
                        if Relation == True:
                            for z in Realtion.set_Relation(PackageList[i], AixLib_path):
                                ClassDiagram.insert_line(PackageList[i],output_path,ClassDiagram.number_of_lines(PackageList[i],output_path)-1,"\n"+z+"\n" )
                                continue
             
        if HierarchyLevel>3:
            for w in range(0,len(Model3),1):
                for i in Realtion.get_Relation(Model3[w],AixLib_path,block):
                    PackageList = []
                    Package = []
                    i= i.split(",")
                    if len(i)==3:
                        filename_input = i[0] 
                        RelationModel = i[1]
                        Package.append(i[2])
                    else:
                        filename_input = i[0] 
                        RelationModel = i[1]
                   
                    RelationModel = filename_input.split(".")
                    RelationModel = RelationModel[0].split("\\")
                    RelationModel = RelationModel[len(RelationModel)-1]
                   
                    T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                    
                 
                    S = DataCheck.getPackagesinPackages(T , output_path)
                   
                    S = (S[0].split("\\"))
                    PackageName = S[len(S)-1].split(".")
                    count = 0
                    xstr = ""
                    for x in PackageName[:-2]:
                        if count == 0:
                            xstr =  xstr+x 
                        else:
                            xstr = xstr +"."+x
                        count = count +1 
                    Package.append(xstr)
                    PackageList = DataCheck.set_ModelsinPackages(T , output_path)
                    
                    for i in range(0,len(PackageList),1):
                        DataCheck.filename_exist(PackageList[i])
                        ClassDiagram.put_full_class(PackageList[i],output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
                        Model4.append(PackageList[i])
                        if Relation == True:
                            for z in Realtion.set_Relation(PackageList[i], AixLib_path):
                                ClassDiagram.insert_line(PackageList[i],output_path,ClassDiagram.number_of_lines(PackageList[i],output_path)-1,"\n"+z+"\n" )
                                continue
                         
        if HierarchyLevel>4:
            for w in range(0,len(Model4),1):
                for i in Realtion.get_Relation(Model4[w],AixLib_path,block):
                    PackageList = []
                    Package = []
                    i= i.split(",")
                    if len(i)==3:
                        filename_input = i[0] 
                        RelationModel = i[1]
                        Package.append(i[2])
                    else:
                        filename_input = i[0] 
                        RelationModel = i[1]
                   
                    RelationModel = filename_input.split(".")
                    RelationModel = RelationModel[0].split("\\")
                    RelationModel = RelationModel[len(RelationModel)-1]
                   
                    T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                    
                 
                    S = DataCheck.getPackagesinPackages(T , output_path)
                   
                    S = (S[0].split("\\"))
                    PackageName = S[len(S)-1].split(".")
                    count = 0
                    xstr = ""
                    for x in PackageName[:-2]:
                        if count == 0:
                            xstr =  xstr+x 
                        else:
                            xstr = xstr +"."+x
                        count = count +1 
                    Package.append(xstr)
                    PackageList = DataCheck.set_ModelsinPackages(T , output_path)
                    
                    for i in range(0,len(PackageList),1):
                        DataCheck.filename_exist(PackageList[i])
                        ClassDiagram.put_full_class(PackageList[i],output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
                        Model5.append(PackageList[i])
                        if Relation == True:
                            for z in Realtion.set_Relation(PackageList[i], AixLib_path):
                                ClassDiagram.insert_line(PackageList[i],output_path,ClassDiagram.number_of_lines(PackageList[i],output_path)-1,"\n"+z+"\n" )
                                continue
        if HierarchyLevel>5:
            for w in range(0,len(Model5),1):
                for i in Realtion.get_Relation(Model5[w],AixLib_path,block):
                    PackageList = []
                    Package = []
                    i= i.split(",")
                    if len(i)==3:
                        filename_input = i[0] 
                        RelationModel = i[1]
                        Package.append(i[2])
                    else:
                        filename_input = i[0] 
                        RelationModel = i[1]
                   
                    RelationModel = filename_input.split(".")
                    RelationModel = RelationModel[0].split("\\")
                    RelationModel = RelationModel[len(RelationModel)-1]
                   
                    T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                    
                 
                    S = DataCheck.getPackagesinPackages(T , output_path)
                   
                    S = (S[0].split("\\"))
                    PackageName = S[len(S)-1].split(".")
                    count = 0
                    xstr = ""
                    for x in PackageName[:-2]:
                        if count == 0:
                            xstr =  xstr+x 
                        else:
                            xstr = xstr +"."+x
                        count = count +1 
                    Package.append(xstr)
                    PackageList = DataCheck.set_ModelsinPackages(T , output_path)
                    
                    for i in range(0,len(PackageList),1):
                        DataCheck.filename_exist(PackageList[i])
                        ClassDiagram.put_full_class(PackageList[i],output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)
                        #Model3.append(PackageList[i])
                        if Relation == True:
                            for z in Realtion.set_Relation(PackageList[i], AixLib_path):
                                ClassDiagram.insert_line(PackageList[i],output_path,ClassDiagram.number_of_lines(PackageList[i],output_path)-1,"\n"+z+"\n" )
                                continue
                    
                    
                    
                  
                      
                   
                    
                    """
                    
                    
                    DataCheck.filename_exist(Model1[w])
                    print(filename_input)
                    RelationModel = RelationModel.split(".")
                    RelationModel = (RelationModel[len(RelationModel)-1])
                    T = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)
                    
                    T= T.split(".")
                 
                    Str = ""
                    count = 0
                    for y in T[:-2]:
                        count = count +1 
                        if count == 1:
                            Str = Str + y
                        else:
                            Str = Str +"." +y
                    
                    #Str = Str +"."+T[-3]
                    Str = Str +".java"
                    T =Str
                    print(T)
                       
                        
                         
                   
                    S = DataCheck.getPackagesinPackages(T , output_path)
                    
                    if len(S)>0:
                        S = (S[0].split("\\"))
                        PackageName = S[len(S)-1].split(".")
                        count = 0
                        xstr = ""
                        for x in PackageName[:-2]:
                            if count == 0:
                                xstr =  xstr+x 
                            else:
                                xstr = xstr +"."+x
                            count = count +1 
                        Package.append(xstr)
                        PackageList = DataCheck.set_ModelsinPackages(T , output_path)
                    #print(Package)
                    filename_input  = ClassConverter.Model_Converter(filename_input,output_path,RelationModel,AixLib_path)  
                    T = ClassDiagram.put_full_class(filename_input,output_path,parameter,variables,primitivevariables,complexvariables,methode,Package,showPackages,Relation,showconstant,showType)  
                    Package = []
                    for i in range(0,len(T),1):
                        Model2.append(T[i])
                        Model21.append(T[i])
                    Model2.append(filename_input)
                
                    for z in Realtion.set_Relation(filename_input, AixLib_path):
                      
                        ClassDiagram.insert_line(filename_input,output_path, ClassDiagram.number_of_lines(filename_input,output_path)-1,"\n"+z+"\n" )
                        continue"""
               
                        
                        
                        
                        
              
        DataCheck.Appender(output_path, finalData)
        UML_Interface.test(finalData,0,"@startuml{")    
        UML_Interface.test(finalData,UML_Interface.test2(finalData), " \n @enduml")  
        UML_Interface.sort(finalData)
        #
        #print(PackageList)
        print("Conversion Erfolgreich!")
        
        




        



filename_input =r"C:\Users\hinack\Dropbox\09_Modelica_Library\Modelica\Fluid\Valves.mo"
#filename_input=  r"C:\Users\sven-\Dropbox\09_Modelica_Library\Modelica\Blocks\Interfaces.mo"

AixLib_path=r"C:\Users\hinack\Dropbox\09_Modelica_Library"
output_path =  r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
finalData = r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil.java"

parameter = False
variables = False

Relation = False

Medium = False
primitivevariables= False
methode = False
complexvariables = False
HierarchyLevel = 2
block = False
showPackages = False 
showconstant = False
showType = False
Package =  []





Instanz = UMLLibraryClassDiagram()
if __name__ == "__main__":
        
     Instanz.Library_Interface(filename_input,output_path,AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation,showconstant,showType)
    # for w in range(1,10,1):
     #   print(type(w))