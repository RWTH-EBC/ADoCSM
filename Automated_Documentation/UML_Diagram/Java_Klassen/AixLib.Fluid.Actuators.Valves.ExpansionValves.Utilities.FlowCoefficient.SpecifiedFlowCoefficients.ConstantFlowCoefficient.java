@startuml




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class ConstantFlowCoefficient << model >>  {
 + parameter Real C_const  {  unit="1", min = 0, max = 100, nominal = 25  }   = 15 
}
}

PartialFlowCoefficient <|---up ConstantFlowCoefficient
@enduml