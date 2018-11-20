from PyQt4.QtGui import QApplication
from PyQt4.uic import loadUi
import sys
Einstellung_name = []  # Definition der Listen
Einstellung_werte = [] 


class Window(object):

    def __init__(self):
        self.ui = loadUi('.txt ')
        self.ui.Button.clicked.connect(self.Schreiben)
        self.ui.Button2.clicked.connect(self.Lesen)
        self.ui.show()
       
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-       
        
#           Position der Einstellungen in der .txt
        global Wassertemp, Fuellstand  # Position der Einstellungen in der .txt
        Wassertemp = 0  # 0 = 1.Zeile in der .txt
        Fuellstand = 1  # 1 = 2.Zeile in der .txt
        # CO2 gehalt=2 usw
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-   

    def Oeffnen(self):       
        del Einstellung_name[:]  # leert die Liste (den Inhalt) der 1.Spalte
        del Einstellung_werte[:]  # leert die Liste (den Inhalt) der 2.Spalte
        Datei = open("Inputdatei.txt", "r")  # r=read
        for line in Datei.readline():  # f�r jeder Zeile in der .txt
            line = line.rstrip()  # rstrip() entfernt unn�tige leerzeichen und \n
            line = line.split("\t")  # f�gt alle Werte der Zeile die mit einem "Tab (\t)" getrennt sind in eine Liste
            Einstellung_name.append(line[0])  # reiht nur die Werte der 1. Spalte aneinander == [0]   
            Einstellung_werte.append(line[1])  # reiht nur die Werte der 2. Spalte aneinander == [1]
        Datei.close()   
        
    def Lesen(self):
        self.Oeffnen()  # Funktion "Oeffnen" starten
        print(Einstellung_name)  # zur Kontrolle ausgegeben
        print(Einstellung_werte)
        self.ui.Optionsfeld1.setText(Einstellung_name[Wassertemp])  # Schreibt die jeweiligen Werte in das Textfeld
        self.ui.Optionsfeld2.setText(Einstellung_name[Fuellstand])
        self.ui.Optionsfeld3.setText(Einstellung_werte[Wassertemp])
        self.ui.Optionsfeld4.setText(Einstellung_werte[Fuellstand])
# _-_-_-_hier analoge Erg�nzung weiterer Einstellungen-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-  
        
    def Schreiben(self):
        self.Oeffnen()  # Funktion "Oeffnen" muss durchgef�rt werden, um die Liste mit den Werten zu f�llen
        # �berpr�fung ob ein Feld leer => sonst wird die .txt leer �berschrieben
# _-_-_-_hier analoge Erg�nzung weiterer Optinsfelder die nicht "leer" sein d�rfen-_-_-_-_-_-_-_-_-_-_-
        if self.ui.Optionsfeld1.text() == "" or self.ui.Optionsfeld2.text() == "" or self.ui.Optionsfeld3.text() == "" or self.ui.Optionsfeld4.text() == "" :
            self.ui.Status.setText("Fehler!!! ein Optionsfeld leer")
        else:
            Datei = open("OutputDatei.txt", "w")  # nachdem die Liste voll ist, wird die Datei neu ge�ffnet mit schreibrechten
            Einstellung_name[Wassertemp] = self.ui.Optionsfeld1.text()  # �bergibt den Inhalt des Textfeldes an die entsprechende stelle in der Liste
            Einstellung_name[Fuellstand] = self.ui.Optionsfeld2.text()
            Einstellung_werte[Wassertemp] = self.ui.Optionsfeld3.text()
            Einstellung_werte[Fuellstand] = self.ui.Optionsfeld4.text()
# _-_-_-_-_-_hier analoge Erg�nzung weiterer Einstellungen-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-  

            for x in range(0, len(Einstellung_name)):  # len(Liste) anzahl der Elemente in der Liste == entspricht der gesamten Zeilenanzahl == start bei x=0 (1.Zeile)
                Zeile_komplett = Einstellung_name[x] + "\t" + Einstellung_werte[x]  # schreibt die jeweiligen Werte der Liste mit einem \t getrennt in die Zeilenvariable (Zeile_komplett)   
                Datei.writelines("%s\n" % Zeile_komplett)  # schreibt Wert in Zeile
                x += 1
            Datei.close()
            self.ui.Status.setText("Einstellungen in die .txt gespeichert")

                
def main():
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()     
 
              
if __name__ == '__main__':
    main()
