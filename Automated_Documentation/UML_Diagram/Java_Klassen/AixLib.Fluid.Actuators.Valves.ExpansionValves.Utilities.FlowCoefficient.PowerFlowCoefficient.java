@startuml




Class PowerFlowCoefficient << model >>  {
 + parameter Types.PowerModels powMod=Types.PowerModels.ShanweiEtAl2005 
 + parameter Real a 
 + parameter Real b [ : ]  
 + parameter Integer nT = size  {  b,1  }   
 + parameter Modelica.SIunits.Diameter dCle = 0.02e-3 
 + parameter Real pDifRat = 0.84 
}

PartialFlowCoefficient <|---up PowerFlowCoefficient
@enduml