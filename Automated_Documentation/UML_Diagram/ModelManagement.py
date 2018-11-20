import os

class ModelManagement():    
    def find_version(self):
        systempath64 = r"C:\Program Files (x86)"
        systempath32 = r"C:\Program Files"
        if os.path.isdir(systempath64):
            dym_path=r"\bin64\Dymola.exe"
            systempath=systempath64
        else:
            dym_path=r"\bin\Dymola.exe"
            systempath=systempath32
        temp_list=os.listdir(systempath)
        dym_version=[]
        for word in temp_list:
            if "Dymola" in word:
                dym_version.append(word)
            else:
                continue
        del temp_list
        dym_version.sort()
        full_path=systempath+"\\"+dym_version[-1]+dym_path
        self.lineEdit_version.setText(full_path)
        
Instanz= ModelManagement()     
if __name__ == "__main__":
    Instanz.find_version()
    