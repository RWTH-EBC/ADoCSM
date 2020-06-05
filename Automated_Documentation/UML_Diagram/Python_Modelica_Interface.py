import os
import sys
from fileinput import filename
from pathlib import Path
import os
import pandas as pd
import collections
from pathlib import Path
import numpy as np

## Search and set Interitance in plantuml syntax
class Inheritance():

    # Gibt mir die Vererbungen im filename_input wieder
    def set_inheritance(filename_input):
        readfile_in = open(filename_input, 'r+')
        array0 = []
        for line in readfile_in.readlines():
            x = line.split()
            x_array = np.asarray(x)
            if len(x_array) > 0:
                if x_array[0] == "extends":
                    array0.append(x_array)
                    y = array0[0][1].split('.')
                    y = np.asarray(y)
                    ExtendedModel = y[len(y) - 1].split(';')
                    ExtendedModel = ExtendedModel[0].split("(") 
                    ExtendedModel = ExtendedModel[0]
                    return ExtendedModel  
    
    # Gleiche Funktion wie oben: Gibt für PlantUML passenden return wieder                                
    def write_inheritance(filename_input):
        readfile_in = open(filename_input, 'r+')
        array0 = []
        mainModel = filename_input
        mainModel = mainModel.split("\\")
        mainModel = mainModel[len(mainModel) - 1].split(".")
        mainModel = mainModel[0]
       
        for line in readfile_in.readlines():
            x = line.split()
            x_array = np.asarray(x)
            if len(x_array) > 0:
                if x_array[0] == "extends":
                    array0.append(x_array)
                    y = array0[0][1].split('.')
                    y = np.asarray(y)
                    ExtendedModel = y[len(y) - 1].split(';')
                    ExtendedModel = ExtendedModel[0].split("(") 
                    ExtendedModel = ExtendedModel[0]
                    inheritance = ExtendedModel + "<|--" + mainModel
                    return inheritance
        
    def set_polymorpishm(filename_input): 
        readfile_in = open(filename_input, 'r+')
        array0 = []                          
        for line in readfile_in.readlines():
            x = line.split()
            x_array = np.asarray(x)   
            if len(x_array) > 0:
                if  x_array[0] == "replaceable" and x_array[1] == "model":
                    array0.append(x_array)
                    y = array0[0][1].split('.')
                    y = np.asarray(y)
                    polymorpishmmodel = y[len(y) - 1].split(';')
                    polymorpishmmodel = polymorpishmmodel[0].split("(") 
                    polymorpishmmodel = polymorpishmmodel[0]
                    pass  
                pass
            pass        

    def write_polymorpishm(filename_input):
        readfile_in = open(filename_input, 'r+')
        array0 = []
        mainModel = filename_input
        mainModel = mainModel.split("\\")
        mainModel = mainModel[len(mainModel) - 1].split(".")
        mainModel = mainModel[0]
       
        for line in readfile_in.readlines():
            x = line.split()
            x_array = np.asarray(x)
            
            # print(x_array)
            if len(x_array) > 0:
                if  x_array[0] == "replaceable" and x_array[1] == "model":
                    array0.append(x_array)
                    print(array0) 
                    y = array0[0][1].split('.')
                    print(y)
                    y = np.asarray(y)
                        
                    ExtendedModel = y[len(y) - 1].split(';')
                    ExtendedModel = ExtendedModel[0].split("(") 
                    ExtendedModel = ExtendedModel[0]
                    # print(ExtendedModel)
                                       
                    inheritance = ExtendedModel + "<|--" + mainModel
                    return inheritance
        
    # Sucht den Pfad des Moduls aus      
    def set_pathExtended(AixLib_path, ExtendedModel): 
        destination = AixLib_path
        
        suffixes = []
        
        for root, dirs, files in os.walk(destination):  # root = Path, dirs = folders, files = files
            for file in Path(str(root)).iterdir():
                
                if file.suffix == '.mo' and file.stem == ExtendedModel:
                                        
                    ExtendedModel_Path = root + '\\' + ExtendedModel + file.suffix
                    return ExtendedModel_Path
                    
                    df = pd.DataFrame([root])
                    df.to_clipboard(index=False, header=False)
                    
    def set_pathPolymormism(AixLib_path, PolyphormismModel): 
        destination = AixLib_path
        
        suffixes = []
        
        for root, dirs, files in os.walk(destination):  # root = Path, dirs = folders, files = files
            for file in Path(str(root)).iterdir():
                
                if file.suffix == '.mo' and file.stem == PolyphormismModel:
                                        
                    PolyphormismModel_Path = root + '\\' + PolyphormismModel + file.suffix
                    return PolyphormismModel_Path
                    
                    df = pd.DataFrame([root])
                    df.to_clipboard(index=False, header=False)
    
    def ersetzen():
       # for old, new in ('[(', '])', '\'"'):
       # data = data.replace(old, new)
        filename = 'parsed_percent.txt'
        in_file = open(filename, 'r')
        data = in_file.read()
        in_file.close()
        for character in "[]'":
            data = data.replace(character, '')
        
        out_file = open(filename, 'w')
        out_file.write(data)
        out_file.close()
    # test()
    
    if __name__ == "__main__":
        AixLib_path = "C:\\Users\\sven-\\Dropbox\\AixLib-development_issue590"
        filename_input = r"C:\Users\sven-\Dropbox\AixLib-development_issue590\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves\IsenthalpicExpansionValve.mo"
        
        set_path(AixLib_path, set_inheritance(filename_input))

          
