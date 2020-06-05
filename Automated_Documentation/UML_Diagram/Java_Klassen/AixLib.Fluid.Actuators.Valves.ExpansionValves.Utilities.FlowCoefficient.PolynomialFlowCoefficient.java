@startuml




Class PolynomialFlowCoefficient << model >>  {
 + parameter Types.PolynomialModels polyMod=Types.PolynomialModels.ShanweiEtAl2005 
 + parameter Real a [ : ]  
 + parameter Real b [ : ]  
 + parameter Integer nT = size  {  a,1  }   
 + parameter Modelica.SIunits.Diameter dCle = 0.02e-3 
 + parameter Real pDifRat = 0.84 
}

PartialFlowCoefficient <|---up PolynomialFlowCoefficient
@enduml