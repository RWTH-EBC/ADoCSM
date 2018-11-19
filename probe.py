from UML_Diagram import General
from UML_Diagram import Object_Oriented_Relations
from UML_Diagram import ClassDiagram

ClassConverter = General.Class_Converter()

Realtion = Object_Oriented_Relations.Relation()
DataCheck = General.DataCheck
ClassDiagram = ClassDiagram.ClassDiagram()


class ClassDiagram_MainInterface():
    
    def Class_Interface(self, filename_input, output_path, AixLib_path):
        DataCheck.AixLibPath_exist(AixLib_path)
        DataCheck.filename_exist(filename_input)
        Model = [filename_input]
        filename_input = ClassConverter.Model_Converter(filename_input, output_path)
        Model.remove(Model[0])
        ClassDiagram.put_full_class(filename_input, output_path)
      
        for z in Realtion.set_Relation(filename_input, AixLib_path):
            DataCheck.filename_exist(filename_input)
            # print(z)+
            ClassDiagram.insert_line(filename_input, output_path, 1, "\n" + z)
        
        for i in Realtion.get_Relation(filename_input, AixLib_path):
           
            DataCheck.filename_exist(filename_input)
           
            filename_input = ClassConverter.Model_Converter(i, output_path)  
            ClassDiagram.put_full_class(filename_input, output_path)  
            Model.append(filename_input)
        
            for z in Realtion.set_Relation(filename_input, AixLib_path):
                ClassDiagram.insert_line(filename_input, output_path, 1, "\n" + z)
        
        n = -1 
        
        while n < len(Model) - 1:
            n = n + 1
        
            for x in Realtion.get_Relation(Model[n], AixLib_path):
           
                if x == None:
                   # filename_input  = ClassConverter.Model_Converter(x,output_path)   
                    continue    
                filename_input = ClassConverter.Model_Converter(x, output_path)  
                ClassDiagram.put_full_class(filename_input, output_path) 
          
                Model.append(filename_input) 
            
                for z in Realtion.set_Relation(filename_input, AixLib_path):
                    ClassDiagram.insert_line(filename_input, output_path, 1, "\n" + z)
                    continue
                  
    def test(self, filename_output, insert_pos, line):
        
        f = open(filename_output, "r+")
        lines = f.readlines()
      
        f.close()
        lines.insert(insert_pos, line)
        f = open(filename_output, 'w')
        f.writelines(lines)
        f.close()
     
    def test2(self, finalData):

        file = open(finalData, "r")
         
        lines = file.readlines()
        numberLines = len(lines)
        return numberLines
        file.close()
    
    
filename_input = r"C:\Users\sven-\Dropbox\09_Modelica_Library\AixLib-issue590_ExpansionValve\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves\IsenthalpicExpansionValve.mo"
# filename_input = r"C:\Users\sven-\Dropbox\AixLib-issue590_ExpansionValve\AixLib\Fluid\Actuators\Valves\ExpansionValves\BaseClasses\PartialIsenthalpicExpansionValve.mo"

filename_output = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\test.txt"
AixLib_path = r"C:\Users\sven-\Dropbox\09_Modelica_Library"
output_path = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
Model = [filename_input]
 
finalData = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamtmodell\Ventil.java"

# print("start")    
Instanz = ClassDiagram_MainInterface()

Instanz.Class_Interface(filename_input, output_path, AixLib_path)  
DataCheck.Appender(output_path, finalData)

Instanz.test(finalData, 0, "@startuml{")    

Instanz.test(finalData, Instanz.test2(finalData), " \n @enduml")  

print("Conversion Erfolgreich!")

