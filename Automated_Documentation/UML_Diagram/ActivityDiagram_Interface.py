from UML_Diagram import General
from UML_Diagram import Object_Oriented_Relations
from UML_Diagram import ClassDiagram
#from UML_Diagram import UMLClassDiagram_MainInterface
import os
import shutil

ClassConverter = General.Class_Converter()
Realtion =  Object_Oriented_Relations.Relation()
DataCheck = General.DataCheck
ClassDiagram = ClassDiagram.ClassDiagram()
#UMLClassDiagram_MainInterface = UML_Interace.UMLClassDiagram_MainInterface()


class ActivityDiagram():
    
    def ActivityDiagram_UML(self,filename_input,filename_output):
        readfile_in =open(filename_input,"r")
        readfile_out= open(filename_output,"w")
        for line in readfile_in.readlines():
            print(line)
            
        
















if __name__ == "__main__":  
    Instanz = ActivityDiagram() 
	Instanz.ActivityDiagram_UML(filename_input, filename_output)