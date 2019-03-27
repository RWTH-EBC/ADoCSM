import os
import shutil
import numpy as np
from pathlib import Path
import linecache
from UML_Diagram import General
from UML_Diagram import ClassDiagram

ClassConverter = General.Class_Converter()
ClassDiagram = ClassDiagram.ClassDiagram()
DataCheck = General.DataCheck



class UML_ClassDiagram_Interface():
    
    def convertModelicatoSysML(self,filename_input,filename_output):
        DataCheck.filename_exist(filename_input)
        readfile_in = open(filename_input,"r")
        Lines = Instanz.NumberofLines(filename_input)
        ModelList=[]
        ModelRowList= []
        generalization = []
        Composition = []
        AreaList = []
        Compare = []
        Abstraction = []
        ProfilePartial = []
        enumList = []
        readfile_out = open(filename_output,"w")
        ClassCounter = []
        counter = 0
        readfile_out.write('<?xml version="1.0" encoding="UTF-8"?>')
        readfile_out.write('\n<xmi:XMI xmi:version="20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Modelica4SysML="http:///schemas/Modelica4SysML/_Oq8REN7HEeicI-a70S-euA/2" xmlns:ecore="http://www.eclipse.org/emf/2002/Ecore" xmlns:uml="http://www.eclipse.org/uml2/5.0.0/UML" xsi:schemaLocation="http:///schemas/Modelica4SysML/_Oq8REN7HEeicI-a70S-euA/2 Modelica4SysML.profile.uml#_Oq8REd7HEeicI-a70S-euA">')
        #Muss angepasst werden
        readfile_out.write(' \n <uml:Model xmi:id="_8BnUYN6YEeigT7NLOUUnfg" name="PayprusUMLTest" viewpoint="">\n')
        for line in readfile_in.readlines():
            counter =counter+1
            x = line.split()
            x_array = np.asarray(x)
            if len(x_array) > 0:
                #Class
                
                if x_array[0] == "Class":
                    ClassCounter.append(counter)
                    x_array[0] = x_array[0].lstrip()
                    Model = x_array[1]
                    if line.find("<<")>-1:
                        if line.find(">>")>-1:
                            Stereotype = (line[ line.find("<<")+2:line.find(">>")])
                            Stereotype =  Stereotype.lstrip()
                    ModelHeader = '\n    <packagedElement xmi:type="uml:Class" xmi:id="'+Model+'_ID" '+'name="'+Model+'" visibility="public">'
                    ModelRowList.append(counter)
                    ModelList.append(Model)
                    readfile_out.write(ModelHeader)
                    continue
                if x_array[0] == "interface":
                    ClassCounter.append(counter)
                    x_array[0] = x_array[0].lstrip()
                    Model = x_array[1]
                    if line.find("<<")>-1:
                        if line.find(">>")>-1:
                            Stereotype = (line[ line.find("<<")+2:line.find(">>")])
                            Stereotype =  Stereotype.lstrip()
                    ModelHeader = '\n    <packagedElement xmi:type="uml:Interface" xmi:id="'+Model+'_ID" '+'name="'+Model+'" visibility="public">'
                    ModelRowList.append(counter)
                    ModelList.append(Model)
                    readfile_out.write(ModelHeader)
                    continue
      
                if x_array[0] == "enum":
                    enumList  = []
                    ClassCounter.append(counter)
                    enumList.append(counter)
                    x_array[0] = x_array[0].lstrip()
                    Model = x_array[1]
                    if line.find("<<")>-1:
                        if line.find(">>")>-1:
                            Stereotype = (line[ line.find("<<")+2:line.find(">>")])
                            Stereotype =  Stereotype.lstrip()
                    ModelHeader = '\n    <packagedElement xmi:type="uml:Enumeration" xmi:id="'+Model+'_ID" '+'name="'+Model+'" visibility="public">'
                    ModelRowList.append(counter)
                    ModelList.append(Model)
                    readfile_out.write(ModelHeader)
                    continue
                if len(enumList)==1:
                        if x_array[0]=='}' and len(ClassCounter)==1:
                            print(line)
                            #ClassCounter = []
                            #enumList = []
                            enumList.append("Text")
                        else:    
                            line = line.replace(",","")
                            Literal = '     <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="'+str(counter)+'" name="'+line.replace('"','&quot;')
                            Literal      =Literal.replace("\n","") +'"/>'
                            NumberLines = Instanz.NumberofLines(filename_output)
                            #Instanz.insert_line(filename_output,NumberLines-1,"\n"+Literal)
                            readfile_out.write("\n"+Literal)
                
                ####Attributes
                ##Public    
                if x_array[0]=="+" and len(ClassCounter)==1:
                    if x_array[1] == "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream":
                        if x_array[2] == "Boolean":
                            AttributeName =   x_array[3].lstrip()
                            Attribute =  x_array[2].lstrip()
                            defaultValue = x_array[5].lstrip()
                            ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterBooleanMiddle1 ='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EBoolean"/>'    
                            ParameterBooleanMiddle2 ='      <defaultValue xmi:type="uml:LiteralBoolean" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterBooleanBody   ='      </ownedAttribute>'
                            readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanMiddle2+"\n"+ParameterBooleanBody)
                            continue
                        
                        if x_array[2] == "Real":
                           
                            AttributeName = x_array[3].lstrip()
                            Attribute =  x_array[2].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+ AttributeName+'" visibility="public">'
                            ParameterBooleanMiddle1='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Real"/>'
                            ParameterBooleanMiddle2='      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterBooleanBody   ='      </ownedAttribute>'
                            readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanMiddle2+"\n"+ParameterBooleanBody)
                            continue
                        
                        if x_array[2] == "Modelica.SIunits.Area":
                        
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            #AreaList.append('   <Modelica4SysML:ModelicaSIunitsArea xmi:id="'+'Modelica.SIunits.Area'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>')
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.Diameter":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.Time":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.MassFlowRate":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.PressureDifference":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Medium.MassFlowRate":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2]  ==   "Integer":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader='         <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1='       <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Integer"/>'
                            #ParameterAreaMiddle2 = '       <defaultValue xmi:type="uml:LiteralInteger" xmi:id='+str(counter)+'_ID"/>'
                            ParameterAreaBody = '      </ownedAttribute>'
                            #readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                           
                            continue
                            
    
                    if x_array[1]  ==   "Integer":
                        AttributeName = x_array[3].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader='         <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1='       <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Integer"/>'
                        ParameterAreaBody = '      </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue     
                    
                    if x_array[1] == "Boolean":
                        AttributeName =   x_array[3].lstrip()
                        Attribute =  x_array[2].lstrip()
                        defaultValue = x_array[5].lstrip()
                        ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterBooleanMiddle1 ='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EBoolean"/>'    
                        ParameterBooleanMiddle2 ='      <defaultValue xmi:type="uml:LiteralBoolean" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterBooleanBody   ='      </ownedAttribute>'
                        readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanBody)
                        continue
                   
                    
                    if x_array[1] == "Real":
                        AttributeName = x_array[2].lstrip()
                        Attribute =  x_array[1].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterBooleanMiddle1='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Real"/>'
                        #ParameterBooleanMiddle2='      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterBooleanBody   ='      </ownedAttribute>'
                        readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanBody)
                        continue
                    
                    if x_array[1] == "Modelica.SIunits.Area":
                        
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        #AreaList.append('   <Modelica4SysML:ModelicaSIunitsArea xmi:id="'+'Modelica.SIunits.Area'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>')
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.Diameter":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.Time":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.MassFlowRate":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.PressureDifference":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Medium.MassFlowRate":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+str(counter)+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                    
  ##################################################################################################################################################                
  ##Protected              
                if x_array[0]=="#" and len(ClassCounter)==1:
                    if x_array[1] == "parameter" or x_array[1] == "input" or x_array[1] == "flow"  or x_array[1] == "stream":
                        if x_array[2] == "Boolean":
                            AttributeName =   x_array[3].lstrip()
                            Attribute =  x_array[2].lstrip()
                            defaultValue = x_array[5].lstrip()
                            ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="protected">'
                            ParameterBooleanMiddle1 ='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EBoolean"/>'    
                            ParameterBooleanMiddle2 ='      <defaultValue xmi:type="uml:LiteralBoolean" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterBooleanBody   ='      </ownedAttribute>'
                            readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanMiddle2+"\n"+ParameterBooleanBody)
                            continue
                        
                        if x_array[2] == "Real":
                           
                            AttributeName = x_array[3].lstrip()
                            Attribute =  x_array[2].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="protected">'
                            ParameterBooleanMiddle1='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Real"/>'
                            ParameterBooleanMiddle2='      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterBooleanBody   ='      </ownedAttribute>'
                            readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanMiddle2+"\n"+ParameterBooleanBody)
                            continue
                        
                        if x_array[2]  ==   "Integer":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader='         <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="protected">'
                            ParameterAreaMiddle1='       <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Integer"/>'
                            #ParameterAreaMiddle2 = '       <defaultValue xmi:type="uml:LiteralInteger" xmi:id='+str(counter)+'_ID" value="'+ defaultValue+'">'
                            #ParameterAreaMiddle2 = '       <defaultValue xmi:type="uml:LiteralInteger" xmi:id='+str(counter)+'_ID"/>'
                            ParameterAreaBody = '      </ownedAttribute>'
                            #readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                            continue
                        
                        if x_array[2] == "Modelica.SIunits.Area":
                        
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            #AreaList.append('   <Modelica4SysML:ModelicaSIunitsArea xmi:id="'+'Modelica.SIunits.Area'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>')
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.Diameter":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.Time":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.MassFlowRate":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Modelica.SIunits.PressureDifference":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                            continue
                        if x_array[2] == "Medium.MassFlowRate":
                            AttributeName = x_array[3].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+str(counter)+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
    
                    
                    if x_array[1] == "Boolean":
                        AttributeName =   x_array[2].lstrip()
                        Attribute =  x_array[2].lstrip()
                        defaultValue = x_array[5].lstrip()
                        ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="protected">'
                        ParameterBooleanMiddle1 ='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EBoolean"/>'    
                        ParameterBooleanMiddle2 ='      <defaultValue xmi:type="uml:LiteralBoolean" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterBooleanBody   ='      </ownedAttribute>'
                        readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanBody)
                        continue
                    
                    if x_array[1] == "Real":
                        AttributeName = x_array[2].lstrip()
                        Attribute =  x_array[1].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterBooleanHeader ='      <ownedAttribute xmi:type="uml:Property" xmi:id="'+ AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="protected">'
                        ParameterBooleanMiddle1='      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Real"/>'
                        #ParameterBooleanMiddle2='      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterBooleanBody   ='      </ownedAttribute>'
                        readfile_out.write("\n"+ParameterBooleanHeader+"\n"+ParameterBooleanMiddle1+"\n"+ParameterBooleanBody)
                        continue
                    
                    if x_array[1]  ==   "Integer":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader='         <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="protected">'
                        ParameterAreaMiddle1='       <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml#Integer"/>'
                        #ParameterAreaMiddle2 = '       <defaultValue xmi:type="uml:LiteralInteger" xmi:id='+str(counter)+'_ID" value="'+ defaultValue+'">'
                        #ParameterAreaMiddle2 = '       <defaultValue xmi:type="uml:LiteralInteger" xmi:id='+str(counter)+'_ID"/>'
                        ParameterAreaBody = '      </ownedAttribute>'
                        #readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaMiddle2+"\n"+ParameterAreaBody)
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                        
                    
                    if x_array[1] == "Modelica.SIunits.Area":
                        
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        #AreaList.append('   <Modelica4SysML:ModelicaSIunitsArea xmi:id="'+'Modelica.SIunits.Area'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>')
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.Diameter":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.Time":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.MassFlowRate":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                        continue
                    if x_array[1] == "Modelica.SIunits.PressureDifference":
                            AttributeName = x_array[2].lstrip()
                            defaultValue = x_array[len(x_array)-1].lstrip()
                            ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                            ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                            ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                            ParameterAreaBody =   '       </ownedAttribute>'
                            readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                            continue
                    if x_array[1] == "Medium.MassFlowRate":
                        AttributeName = x_array[2].lstrip()
                        defaultValue = x_array[len(x_array)-1].lstrip()
                        ParameterAreaHeader =  '      <ownedAttribute xmi:type="uml:Property" xmi:id="'+AttributeName+'_ID" '+'name="'+AttributeName+'" visibility="public">'
                        ParameterAreaMiddle1=  '      <type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloat"/>'
                        ParameterAreaMiddle2=  '      <defaultValue xmi:type="uml:LiteralReal" xmi:id="'+str(counter)+'_ID" value="'+defaultValue+'"/>'
                        ParameterAreaBody =   '       </ownedAttribute>'
                        readfile_out.write("\n"+ParameterAreaHeader+"\n"+ParameterAreaMiddle1+"\n"+ParameterAreaBody)
                    
                ##Operation
                if x_array[0] =="+" and line.find("(")>-1:
                    if len(enumList) != 2: 
                     
                        if x_array[1].find("(")>-1:
                            continue
                        else:
                            x = line.find("+")
                            y = line.find("(")
                           
                            Operation = '      <ownedOperation xmi:type="uml:Operation" xmi:id="'+str(counter)+'" name="'+line[x+2:y]+'" visibility="public"/>'
                            #    print(Operation)
                            readfile_out.write("\n"+Operation)
                            
                            #<ownedOperation xmi:type="uml:Operation" xmi:id="90" name="dp">
                            #<ownedParameter xmi:type="uml:Parameter" xmi:id="_TVXu4OHzEeig0ogs4PqciQ" name="port_a.p">
                            #<type xmi:type="uml:PrimitiveType" href="pathmap://UML_LIBRARIES/EcorePrimitiveTypes.library.uml#EFloatObject"/>
                            #</ownedParameter>
                            #</ownedOperation>
                    
                            #readfile_out.write("\n"+Operation)
                            continue
                    
             
                
                
                
                        
                        
                if len(x_array)>1:            
                    if x_array[1]==  "<|---up" :
                        ModelID = x_array[0]+"_ID"
                        Model = x_array[2]
                        count = 0
                        for x in ModelList:
                            if x == Model:
                                
                                break 
                            count =  count +1
                        generalization.append('\n<generalization xmi:type="uml:Generalization" xmi:id="'+str(counter)+'" general="'+ModelID+'" />\n' +" ; " + Model )
                    if x_array[1]==  "<|..-up" :
                        supplier = x_array[0]+"_ID"
                        Model = x_array[2].split('"')
                        Name = Model[1]
                        client = Model[2]+"_ID"
                      
                        count = 0
                        for x in ModelList:
                            if x == Model:
                                
                                break 
                            count =  count +1
                        Abstraction.append('\n<packagedElement xmi:type="uml:Abstraction" xmi:id="'+str(counter)+'" name="'+Name+'" client="'+client+'" supplier="'+supplier+'"/>')
                       
                    if x_array[1]== "-down--*":
                       
                        ListModel1 = []
                        ListModel2 = []
                        Compare = []
                        #FluidPort_b --* "port_b"PartialTwoPort
                        Model1 = x_array[0].lstrip()
                        array3 = x_array[2].lstrip()
                        array3 = array3.split('"')
                        Model2 = array3[len(array3)-1]
                     
                        ID1 = "Association"+str(counter)
                        ID2 = "Property"+str(counter)
                        assocationID = "assocationID"+str(counter)
                        
                        ###Model2
                        ListModel2.append('    <ownedAttribute xmi:type="uml:Property" xmi:id="'+ID1+'" name="'+Model1+'" type="'+Model1+'_ID" aggregation="composite" association="'+assocationID+'">')
                        ListModel2.append('      <lowerValue xmi:type="uml:LiteralInteger" xmi:id="'+"Compositon"+str(counter)+'" value="1"/>')
                        ListModel2.append('      <upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="'+"Compositon"+str(counter+1)+'" value="*"/>')
                        ListModel2.append('    </ownedAttribute>')
                        
                        ##Model1
                        ListModel1.append('    <ownedAttribute xmi:type="uml:Property" xmi:id="'+"Compositon"+str(counter+2)+'" name="'+Model2+'" type="'+Model2+'_ID">')
                        ListModel1.append('      <lowerValue xmi:type="uml:LiteralInteger" xmi:id="'+"Compositon"+str(counter+3)+'"/>')
                        ListModel1.append('      <upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="'"Compositon"+str(counter+4)+'" value="1"/>')
                        ListModel1.append('     </ownedAttribute>')
                        
                        ##Composition
                        Composition.append('     <packagedElement xmi:type="uml:Association" xmi:id="'+assocationID+'" memberEnd="'+ID1+" "+ID2+'">')
                        Composition.append('     <eAnnotations xmi:type="ecore:EAnnotation" xmi:id="'+"Compositon"+str(counter+5)+'" source="org.eclipse.papyrus">')
                        Composition.append('     <details xmi:type="ecore:EStringToStringMapEntry" xmi:id="'+"Compositon"+str(counter+6)+'" key="nature" value="UML_Nature"/>')
                        Composition.append('     </eAnnotations>')
                        Composition.append('     <ownedEnd xmi:type="uml:Property" xmi:id="'+ID2+'" name="'+Model2+'" type="'+Model2+'_ID" association="'+assocationID+'"/>')
                        Composition.append('      </packagedElement>')
                        
                        Compare.append(Model1+","+Model2)
                       
                        
                        readfile_out.close()
                        readfile_out = open(filename_output,"r+")
                        
                        
                        count = 0
                        for lines in readfile_out.readlines():
                            count = count +1
                            x = lines.split()
                            x_array = np.asarray(x)
                            for w in Compare:
                                w = w.split(",")
                                Model1Name = w[0]
                                Model2Name = w[1]
                                if len(x_array)>3: 
                                    if x_array[3] == 'name="'+Model1Name+'"':
                                        for x in ListModel1:
                                          
                                           
                                            Instanz.insert_line(filename_output, count, x+"\n")
                                            count = count +1
                        
                        
                        readfile_out.close()
                        readfile_out = open(filename_output,"r+")
                        count = 0
                        for lines in readfile_out.readlines():
                            count = count +1
                            x = lines.split()
                            x_array = np.asarray(x)
                            for w in Compare:
                                w = w.split(",")
                                Model1Name = w[0]
                                Model2Name = w[1]
                                if len(x_array)>3: 
                                    if x_array[3] == 'name="'+Model2Name+'"':
                                        for x in ListModel2:
                                          
                                           
                                            Instanz.insert_line(filename_output, count, x+"\n")
                                            count = count +1
                  
                  
                  
                  
                        
                
                if x_array[0]=="}" and len(ClassCounter)==1:
                    ClassCounter = []
                    enumList = []
                    readfile_out.write('\n    </packagedElement>')
                    continue
                
                #if counter == Lines:
                 #   readfile_out.write('\n    </uml:Model>')
                  #  readfile_out.write('\n</xmi:XMI>')
                    
           
                            
          
                          
        readfile_in.close()
        readfile_out.close()
        readfile_in = open(filename_output,"r+")
        count = 0
        for line in readfile_in.readlines():
            count = count +1
            x = line.split()
            x_array = np.asarray(x)
            for w in generalization:
                T = w.split(";")
                RelationText = T[0].lstrip()
                Model = T[1].lstrip()
                if len(x_array)>3:
                    if x_array[3] == 'name="'+Model+'"':
                        Instanz.insert_line(filename_output,count,"    "+RelationText)
                        count = count +1
                        break
                    else:
                        continue
        readfile_in.close()
        readfile_in = open(filename_output,"r+")
  
        count= 0
        for w in Abstraction:
            w = w.lstrip()
        
           
            if count == 0:
                NumberLines = Instanz.NumberofLines(filename_output)
                Instanz.insert_line(filename_output,NumberLines,"\n    "+w+"\n")
            else:
                NumberLines = Instanz.NumberofLines(filename_output)
                Instanz.insert_line(filename_output,NumberLines,"    "+w+"\n")
                
            count=    count +1
        
        count= 0
        for C in Composition:
            C = C.lstrip()
           
            if count == 0:
                NumberLines = Instanz.NumberofLines(filename_output)
                Instanz.insert_line(filename_output,NumberLines,"\n    "+C+"\n")
            else:
                NumberLines = Instanz.NumberofLines(filename_output)
                Instanz.insert_line(filename_output,NumberLines,"    "+C+"\n")
            count  =  count +1
           
        
        
        
    def converter(self,filename_input,filename_output):
        readfile_in = open(filename_input,"r")
        readfile_out = open(filename_output,"w")
        for line in readfile_in.readlines():
            line = line.replace("="," = ")
           
            readfile_out.write(line)
            continue
        readfile_in.close()
        readfile_out.close()
        
    def NumberofLines(self,filename_input):
        readfile_in = open(filename_input,"r")
        lines = readfile_in.readlines()
        numberLines =  len(lines)
        readfile_in.close()
        return numberLines
        
    def set_Relation(self):
        Instanz.convertModelicatoSysML
        readfile_in = open(filename_input,"a")

   
    def insert_line(self,filename,insert_pos, line):
        f = open(filename, "r+")
        lines = f.readlines()
        f.close()
        lines.insert(insert_pos, line)
        f = open(filename, "w")
        f.writelines(lines)
        f.close()
        
   
    
    def setprofileApplication(self,filename_input,filename_output):
        ProfilePartial = []
        readfile_in = open(filename_input,"r")
        count = 0
        ProfilePartial.append('    <profileApplication xmi:type="uml:ProfileApplication" xmi:id="'+str(count)+'">')
        ProfilePartial.append('     <eAnnotations xmi:type="ecore:EAnnotation" xmi:id="'+str(count)+'" source="http://www.eclipse.org/uml2/2.0.0/UML">')
        ProfilePartial.append('        <references xmi:type="ecore:EPackage" href="Modelica4SysML.profile.uml#_znl6Ed93Eei2AdFulrt0aQ"/>')
        ProfilePartial.append('     </eAnnotations>')
        ProfilePartial.append('        <appliedProfile xmi:type="uml:Profile" href="Modelica4SysML.profile.uml#_zAFOIN93Eei2AdFulrt0aQ"/>')
        ProfilePartial.append('    </profileApplication>')
        for x in ProfilePartial:
            Instanz.insert_line(filename_output,Instanz.NumberofLines(filename_output),x+'\n')
            
        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),'    </uml:Model>\n')
        for line in readfile_in.readlines():
            count =  count +1
            x = line.split()
            x_array = np.asarray(x)
            if len(x_array)>3:
                ##StereotTypes
                if x_array[3]=="partial":
                    Model = x_array[1].lstrip()
                    SetProfilePartial = '     <Modelica4SysML:Partial xmi:id="'+str(count)+'" base_Class="'+Model+'_ID'+'"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfilePartial+'\n')
                    continue
                if x_array[3]=="connector":
                    Model = x_array[1].lstrip()
                    SetProfileConnector = '     <Modelica4SysML:Connector xmi:id="'+str(count)+'" base_Interface="'+Model+'_ID'+'"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileConnector+'\n')
                    continue
                  
                if x_array[3]=="type":
                    Model = x_array[1].lstrip()
                    SetProfileEnumeration = '     <Modelica4SysML:type xmi:id="'+str(count)+'" base_Enumeration="'+Model+'_ID'+'"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileEnumeration+'\n')
                    continue
                
                if x_array[3]=="model":
                    Model = x_array[1].lstrip()
                    SetProfileModel = '     <Modelica4SysML:Model xmi:id="'+str(count)+'" base_Class="'+Model+'_ID'+'"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModel+'\n')
                    continue
                if x_array[2] == "Modelica.SIunits.Area":
                    if  x_array[1] ==  "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream" :
                        AttributeName = x_array[3].lstrip()
                        SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsArea xmi:id="'+'Modelica.SIunits.Area'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                        continue      
                if  x_array[2] == "Modelica.SIunits.Diameter":
                    if x_array[1] == "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream":
                       
                        AttributeName = x_array[3].lstrip()
                        SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsDiameter xmi:id="'+'Modelica.SIunits.Diameter'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                        continue  
                if x_array[2] == "Modelica.SIunits.Time":
                    if  x_array[1] == "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream":
                        AttributeName = x_array[3].lstrip()
                        SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsTime xmi:id="'+'Modelica.SIunits.Time'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                        continue
                if x_array[2] == "Modelica.SIunits.MassFlowRate":
                    if x_array[1] == "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream":
                        AttributeName = x_array[3].lstrip()
                        SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsMassFlowRate xmi:id="'+'Modelica.SIunits.MassFlowRate'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                        continue  
                if x_array[2] == "Modelica.SIunits.PressureDifference":
                    if x_array[1] == "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream" :
                        AttributeName = x_array[3].lstrip()
                        SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsPressureDifference xmi:id="'+'Modelica.SIunits.PressureDifference'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                        continue 
                if x_array[2] == "Medium.MassFlowRate":
                    if  x_array[1] == "parameter" or x_array[1] == "input"  or x_array[1] == "flow"  or x_array[1] == "stream" :
                        AttributeName = x_array[3].lstrip()
                        SetProfileModelicaArea = '     <Modelica4SysML:MediumMassFlowRate xmi:id="'+'Medium.MassFlowRate'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                        continue
                if x_array[1] == "Modelica.SIunits.Area":
                    AttributeName = x_array[2].lstrip()
                    SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsArea xmi:id="'+'Modelica.SIunits.Area'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                    continue      
                if x_array[1] == "Modelica.SIunits.Diameter":
                    AttributeName = x_array[2].lstrip()
                    SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsDiameter xmi:id="'+'Modelica.SIunits.Diameter'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                    continue  
                if  x_array[1] == "Modelica.SIunits.Time":
                    AttributeName = x_array[2].lstrip()
                    SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsTime xmi:id="'+'Modelica.SIunits.Time'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                    continue
                if x_array[1] == "Modelica.SIunits.MassFlowRate":
                    AttributeName = x_array[2].lstrip()
                    SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsMassFlowRate xmi:id="'+'Modelica.SIunits.MassFlowRate'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                    continue  
                if x_array[1] == "Modelica.SIunits.PressureDifference":
                    AttributeName = x_array[2].lstrip()
                    SetProfileModelicaArea = '     <Modelica4SysML:ModelicaSIunitsPressureDifference xmi:id="'+'Modelica.SIunits.PressureDifference'+str(count)+'_ID" '+'base_Property="'+AttributeName+'_ID"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                    continue 
                if x_array[1] == "Medium.MassFlowRate":
                    
                    AttributeName = x_array[2].lstrip()
                    SetProfileModelicaArea = '     <Modelica4SysML:MediumMassFlowRate xmi:id="'+'Medium.MassFlowRate'+str(count)+'_ID" '+'base_Property="'+AttributeName+str(count)+'_ID"/>'
                    Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),SetProfileModelicaArea+'\n')
                    continue   
                          
                       
                   
                    
        Instanz.insert_line(filename_output, Instanz.NumberofLines(filename_output),'</xmi:XMI>')        
          
                    
                 


filename_input = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\Ventil2.java"       

filename_output = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\UML\UML.txt"
filename_output2 = r"C:\Users\sven-\Dropbox\08_Eclipse_Workspace_Automated_Documentation\Automated_Documentation\UML_Diagram\Java_Klassen\Gesamt\UML\UML.uml"
Instanz = UML_ClassDiagram_Interface()

if __name__ == "__main__":
    Instanz.converter(filename_input,filename_output)
  
    Instanz.convertModelicatoSysML(filename_output,filename_output2)
    Instanz.setprofileApplication(filename_output,filename_output2)
    print("Finish")