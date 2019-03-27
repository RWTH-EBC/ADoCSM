import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from UML_Diagram import  UML_Interface
from UML_Diagram import General
from importlib.resources import path
from UML_Diagram import  UML_Library
import subprocess



class Thread(QtCore.QThread):
    def run(self):
        QtCore.QThread.sleep(2)

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()
    def initMe(self):
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1309, 756)
        #self.centralWidget = QtWidgets.QWidget(MainWindow)
        #self.centralWidge.setObjectName("centralWidget")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        
        self.checkBox = QtWidgets.QCheckBox("show Parameter",self)
        self.checkBox.setGeometry(QtCore.QRect(30, 110, 121, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(lambda:self.showParamter(self.checkBox))
        
        self.checkBox_2 = QtWidgets.QCheckBox("show constants",self)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 130, 101, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(lambda:self.showParamter(self.checkBox_2))
        
        
        self.checkBox_3 = QtWidgets.QCheckBox("show variables",self)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 150, 101, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(lambda:self.showParamter(self.checkBox_3))
        
        self.checkBox_4 = QtWidgets.QCheckBox("show primitive variables",self)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 170, 151, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.stateChanged.connect(lambda:self.showParamter(self.checkBox_4))
        
        self.checkBox_5 = QtWidgets.QCheckBox("show complex variables",self)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 190, 151, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.stateChanged.connect(lambda:self.showParamter(self.checkBox_5))
        
        self.checkBox_6 = QtWidgets.QCheckBox("show methode",self)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 210, 151, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.stateChanged.connect(lambda:self.showParamter(self.checkBox_6))
        
        
        self.checkBox_7 = QtWidgets.QCheckBox("show Block",self)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 230, 151, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_7.stateChanged.connect(lambda:self.showParamter(self.checkBox_7))

        self.checkBox_8 = QtWidgets.QCheckBox("show Packages",self)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 250, 151, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_8.stateChanged.connect(lambda:self.showParamter(self.checkBox_8))
        
        self.checkBox_9 = QtWidgets.QCheckBox("show Relation (Initial values)",self)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 270, 160, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_9.stateChanged.connect(lambda:self.showParamter(self.checkBox_9))
        
        self.checkBox_10 = QtWidgets.QCheckBox("show types",self)
        self.checkBox_10.setGeometry(QtCore.QRect(30, 290, 160, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_10.stateChanged.connect(lambda:self.showParamter(self.checkBox_10))
        #self.graphicsView = QtWidgets.QGraphicsView(self)
        #self.graphicsView = pg.PlotWidget(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(460, 40, 1000, 800))
        #self.graphicsView.setObjectName("graphicsView")
        
       
        

        self.pushButton = QtWidgets.QPushButton("Generate Diagram",self)
        self.pushButton.setGeometry(QtCore.QRect(200, 40, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ClassDiagram)
        
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, 150, 31))
        self.comboBox.setMaxVisibleItems(7)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Class Diagram")
        self.comboBox.addItem("Activity Diagram")
        self.comboBox.addItem("Library Class Diagram")
        self.comboBox.activated.connect(self.gettext_combobox)
        
        #text = str(self.comboBox.currentText())
       
        
        
        self.HierachyEbene = QtWidgets.QSpinBox(self)
        self.HierachyEbene.setGeometry(QtCore.QRect(200, 100, 200, 20))
        self.HierachyEbene.setObjectName("hierarchy level")
        self.HierachyEbene.valueChanged.connect(self.Hierchy)
        
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(30, 640, 400, 200))
        self.textBrowser.setObjectName("textBrowser")
        #self.textBrowser.checked.connect(self.pressconsole)
        #self.textBrowser.setText(self.ClassDiagram())
        
        self.label11 =  QtWidgets.QLabel("Console",self)
        self.label11.setGeometry(QtCore.QRect(30, 600, 50, 50))
        
        #self.buttonBox = QtWidgets.QDialogButtonBox(self)
        #self.buttonBox.setGeometry(QtCore.QRect(220, 130, 156, 23))
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.setObjectName("buttonBox")
        
        self.label = QtWidgets.QLabel("Input File",self)
        self.label.setGeometry(QtCore.QRect(20, 350, 91, 16))
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel("Output File",self)
        self.label_2.setGeometry(QtCore.QRect(20, 380, 131, 16))
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_4 = QtWidgets.QLabel("Model Library",self)
        self.label_4.setGeometry(QtCore.QRect(20, 410, 131, 16))
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel("Final Data",self)
        self.label_5.setGeometry(QtCore.QRect(20, 440, 101, 16))
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        
        
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setIcon(QIcon(QPixmap("Ordner.png")))
        self.pushButton_2.setGeometry(QtCore.QRect(410, 350, 20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.loadFileInput)
        
        self.label1 = QtWidgets.QLineEdit(self)
        self.label1.setGeometry(QtCore.QRect(120, 350, 281, 20))
        self.label1.setReadOnly(True)
                                                                                                                    
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setIcon(QIcon(QPixmap("Ordner.png")))
        self.pushButton_3.setGeometry(QtCore.QRect(410, 440, 20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.loadFileFinalData)
        
        self.label2 = QtWidgets.QLineEdit(self)
        self.label2.setGeometry(QtCore.QRect(120, 440, 281, 20))
        self.label2.setReadOnly(True)
        
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setIcon(QIcon(QPixmap("Ordner.png")))
        self.pushButton_4.setGeometry(QtCore.QRect(410, 380, 20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.loadFileOutput)
        
        self.label3 = QtWidgets.QLineEdit(self)
        self.label3.setGeometry(QtCore.QRect(120, 380, 281, 20))
        self.label3.setReadOnly(True)
       
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setIcon(QIcon(QPixmap("Ordner.png")))
        self.pushButton_5.setGeometry(QtCore.QRect(410, 410, 20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.loadFileModelLibrary)
       
        self.label4 = QtWidgets.QLineEdit(self)
        self.label4.setGeometry(QtCore.QRect(120, 410, 281, 20))
        self.label4.setReadOnly(True)
       
        #self.label_3 = QtWidgets.QLabel("UML Diagram",self)
        #self.label_3.setGeometry(QtCore.QRect(800, 20, 111, 16))
        #self.label_3.setFont(font)
        #self.label_3.setObjectName("label_3")
        
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        
        
        self.label_6 = QtWidgets.QLabel("Hierarchy level",self)
        self.label_6.setGeometry(QtCore.QRect(250, 80, 111, 16))
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        #self.pushButton_6 = QtWidgets.QPushButton("Load PNG",self)
        #self.pushButton_6.setGeometry(QtCore.QRect(850, 850, 100, 20))
        #self.pushButton_6.setObjectName("pushButton_6")
        #self.pushButton_6.setText("Ventil.png")
        #self.pushButton_6.clicked.connect(self.loadpng)
        
        #self.pushButton_7 =  QtWidgets.QPushButton("Browse",self)
        #self.pushButton_7.setGeometry(QtCore.QRect(800, 900, 200, 20))
        #self.pushButton_7.setObjectName("pushButton_7")
        #self.pushButton_7.setText("Open PlantUML.jar")
        #self.pushButton_7.clicked.connect(self.openPlantUML)
       
        #MainWindow.setCentralWidget(self)
        #self.menuBar = QtWidgets.QMenuBar(MainWindow)
        #self.menuBar.setGeometry(QtCore.QRect(0, 0, 1309, 21))
        #self.menuBar.setObjectName("menuBar")
        #self.menuDiagram_Generator = QtWidgets.QMenu(self.menuBar)
        #self.menuDiagram_Generator.setObjectName("menuDiagram_Generator")
        
        #self.menuOptions = QtWidgets.QMenu(self.menuBar)
        #self.menuOptions.setObjectName("menuOptions")
        
        self.mainToolBar = QtWidgets.QToolBar()
        self.mainToolBar.setObjectName("mainToolBar")
        #MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setObjectName("statusBar")
        #MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar()
        self.toolBar.setObjectName("toolBar")
        #MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionimport = QtWidgets.QAction()
        self.actionimport.setObjectName("actionimport")
        #self.menuDiagram_Generator.addAction(self.actionimport)
        #self.menuBar.addAction(self.menuDiagram_Generator.menuAction())
        #self.menuBar.addAction(self.menuOptions.menuAction()
        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName()
        #self.label10 = QLabel(self)
        #self.label10.setPixmap(QPixmap("Ventil.png"))
        
        #self.label10.setGeometry(700,300,1000,600)
        
        #self.graphic = QtGui.QGuiApplication.
        
        self.setWindowTitle("ADoCSM (automated docu of complex simulation models)")
        self.setWindowIcon(QIcon("EBC_Logo.png"))
        self.setGeometry(50,50,1000,1000)
        self.show()
    
    
    
    
    def plotPng(self):
        self.graphicsView.plot("Ventil.png")
    
        
    def ClassDiagram(self):
        filename_input = window.checkloadInput()
        if len(filename_input)>0:
            filename_input = filename_input
            filename_input= filename_input.replace("/", "\\")
        else:
            filename_input = window.loadFileInput()
            filename_input= filename_input.replace("/", "\\")
        
        output_path = window.checkloadFileOutput()
        if len(output_path)>0:
            output_path = output_path
            output_path = output_path.replace("/","\\")
        else:    
            output_path = window.loadFileOutput()
            output_path = output_path.replace("/","\\")
        
        AixLib_path = window.checkloadFileModelLibrary()
        if len(AixLib_path)>0:
            AixLib_path = AixLib_path
            AixLib_path = AixLib_path.replace("/","\\")
        else:
            AixLib_path = window.loadFileModelLibrary()
            AixLib_path = AixLib_path.replace("/","\\")
        
        finalData = window.checkloadFileFinalData()
        if len(finalData)>0:
            finalData = finalData
            finalData =finalData.replace("/","\\")
        else:
            finalData = window.loadFileFinalData()
            finalData =finalData.replace("/","\\")
        #finalData = r"C:\Users\hinack\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamtmodell\Ventil.java"
        HierarchyLevel = window.Hierchy()
        if HierarchyLevel == 0:
            HierarchyLevel = 1
        #filename_input = r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves\IsenthalpicExpansionValve.mo"
        #output_path =  r"C:\Users\\sven hinrichs\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
        #finalData = r"C:\Users\sven hinrichs\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil.java"
#
        #AixLib_path=r"C:\Users\sven hinrichs\Dropbox\09_Modelica_Library"
        text = self.gettext_combobox()
        if text == "Class Diagram":
            try:
                parameter = window.showParamter(self.checkBox)
                showconstant = window.showParamter(self.checkBox_2)
                variables = window.showParamter(self.checkBox_3)
                primitivevariables = window.showParamter(self.checkBox_4)
                complexvariables = window.showParamter(self.checkBox_5)
                methode = window.showParamter(self.checkBox_6)
                block = window.showParamter(self.checkBox_7)
                showPackages = window.showParamter(self.checkBox_8)
                Relation = window.showParamter(self.checkBox_9)
                showType =  window.showParamter(self.checkBox_10)
               
                print("start")  
                Interface.Class_Interface(filename_input,output_path,AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation,showconstant,showType)
                DataCheck.Appender(output_path, finalData)
                Interface.test(finalData,0,"@startuml")
                Interface.test(finalData,Interface.test2(finalData), " \n @enduml")
                Interface.sort(finalData)
                print("Conversation successful!")
                self.textBrowser.append("Generate ClassDiagram")
                #self.textBrowser.setSource(HierarchyLevel)
               
                #self.textBrowser.append(methode)
                #self.textBrowser.append("\nParameter : "+parameter)
                #self.textBrowser.append("\nVariables : "+variables)
                #self.textBrowser.append("\\nPrimitivevariables : "+primitivevariables)
                #self.textBrowser.append("\nBlock : "+block)
                #self.textBrowser.append("\nComplexvariables : "+complexvariables)
                #self.textBrowser.append("\nMethode : "+methode)
                #self.textBrowser.append("\nFinal Data : "+finalData)
                #self.textBrowser.append("Conversation successful!")
            except :
                 self.textBrowser.append("There was an error!")
        if text == "Library Class Diagram":
            try:
                parameter = window.showParamter(self.checkBox)
                showconstant = window.showParamter(self.checkBox_2)
                variables = window.showParamter(self.checkBox_3)
                primitivevariables = window.showParamter(self.checkBox_4)
                complexvariables = window.showParamter(self.checkBox_5)
                methode = window.showParamter(self.checkBox_6)
                block = window.showParamter(self.checkBox_7)
                showPackages = window.showParamter(self.checkBox_8)
                Relation = window.showParamter(self.checkBox_9)
                showType =  window.showParamter(self.checkBox_10)
                print("start")
                
                Library.Library_Interface(filename_input,output_path,AixLib_path,HierarchyLevel,parameter,variables,primitivevariables,complexvariables,methode,block,showPackages,Relation,showconstant,showType)
                
                print("Conversation successful!")
                self.textBrowser.append("Generate Library Class Diagram")
            
            
            
            except :
                self.textBrowser.append("There was an error!")
            
    def loadFileInput(self):
        fd = QFileDialog()
        fname = fd.getOpenFileName(self, 'Load Input file' ,'D:\03_UML_Klassendiagram\09_Modelica_Library\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves',"(*.mo )")
        self.label1.setText(fname[0])
        return fname[0]
    def checkloadInput(self):
        return self.label1.text()
    def loadFileOutput(self):
        path = QFileDialog.getExistingDirectory(self,"Choose Output directory","D:\03_UML_Klassendiagram")
        self.label3.setText(path)
        return path
    def checkloadFileOutput(self):
        return  self.label3.text()
    def loadFileModelLibrary(self):
        path = QFileDialog.getExistingDirectory(self,"Choose Modellibrary directory","D:\03_UML_Klassendiagram")
        self.label4.setText(path)
        return path
    def checkloadFileModelLibrary(self):
        return self.label4.text()
    def loadFileFinalData(self):
        fd = QFileDialog()
        fname = fd.getOpenFileName(self, 'Set Final file' ,'D:\03_UML_Klassendiagram\Gesamt',"(*.java )")
        self.label2.setText(fname[0])
        return fname[0]
    def checkloadFileFinalData(self):
        return self.label2.text()
        
    def showParamter(self,b):
        if b.text() == "show Parameter":
            if b.isChecked() == True:
                parameter = True
                return parameter
            else:
                parameter = False
                return  parameter
        if b.text() == "show constants":
            if b.isChecked() == True:
                return True
            else:
                return False
        if b.text() == "show variables":
            if b.isChecked() == True:
                return True
            else:
                return False
        if b.text() == "show primitive variables":
            if b.isChecked() == True:
               
                return True
            else:
                return False
        if b.text() == "show complex variables":
            if b.isChecked() == True:
               
                return True
            else:
                return False
        if b.text() == "show methode":
            if b.isChecked() == True:
                return True
            else:
                return False
        if b.text() == "show Block":
            if b.isChecked() == True:
                return True
            else:
                return False
        if b.text() == "show Packages":
            if b.isChecked() == True:
                return True
            else:
                return False
        if b.text() == "show Relation (Initial values)":
            if b.isChecked() == True:
                return True
            else:
                return False 
        if b.text() == "show types":
            if b.isChecked() == True:
                return True
            else:
                return False 
        
        
        #   print("test2")
        #if up:
         #   print("test")
        
    
    def loadpng(self):
        fd = QFileDialog()
        fname = fd.getOpenFileName(self, 'Load Data' ,'Dropbox',"(*.png)")
        fname = fname[0].replace("/","\\")
        print(fname)
        
    def openPlantUML(self):
        self.pushButton_7.setDisabled(True)
        subprocess.call(['Java', '-jar', 'C:\\Users\\sven-\\Dropbox\\14_jd\\plantuml.jar'])
        
    def gettext_combobox(self):
        text = (str(self.comboBox.currentText()))
        
        return text
        
    def Hierchy(self):
        self.HierachyEbene.setRange(1,10)
        return (self.HierachyEbene.value())
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "show parameter"))
        self.checkBox_2.setText(_translate("MainWindow", "show constants"))
        self.checkBox_3.setText(_translate("MainWindow", "show variables"))
        self.checkBox_4.setText(_translate("MainWindow", "show primitive variables"))
        self.checkBox_5.setText(_translate("MainWindow", "show complex variables"))
        self.pushButton.setText(_translate("MainWindow", "Generate Diagram"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Class Diagram"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Activity Diagram"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Other Diagram"))
        self.label.setText(_translate("MainWindow", "InputFile"))
        self.label_2.setText(_translate("MainWindow", "OutputFile"))
        self.label_4.setText(_translate("MainWindow", "Model Library"))
        self.label_5.setText(_translate("MainWindow", "FinalData"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.pushButton_5.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "UML Diagram"))
        self.label_6.setText(_translate("MainWindow", "hierarchy level"))
        #self.pushButton_6.setText(_translate("MainWindow", "Browse"))
        self.menuDiagram_Generator.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionimport.setText(_translate("MainWindow", "import"))

    
#filename_input = r"C:\Users\sven-\Dropbox\09_Modelica_Library\AixLib\Fluid\Actuators\Valves\ExpansionValves\SimpleExpansionValves\IsenthalpicExpansionValve.mo"
#filename_output= r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"

#AixLib_path=r"C:\Users\sven-\Dropbox\09_Modelica_Library"

#output_path =  r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen"
#Model = [filename_input]
#finalData = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamtmodell\Ventil.java"
#HierarchyLevel = 6

Interface = UML_Interface.UMLClassDiagram_MainInterface()
Library = UML_Library.UMLLibraryClassDiagram()
DataCheck = General.DataCheck
#Interface.Class_Interface(filename_input,output_path,AixLib_path,HierarchyLevel)


if __name__ == "__main__":
 


    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    #window.ClassDiagram(filename_input, output_path, AixLib_path, finalData,HierarchyLevel)
    #window.CheckloadFileInput()
    #window.ClassDiagram()
    
    #subprocess.call(['Java', '-jar', 'C:\\Users\\sven-\\Dropbox\\14_jd\\plantuml.jar'])
    sys.exit(app.exec_())