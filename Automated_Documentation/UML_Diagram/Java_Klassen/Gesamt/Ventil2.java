@startuml




 Class PartialFlowCoefficient << partial >>  {
}






 Class PartialExpansionValve << partial >>  {
}












 Class PartialIsenthalpicExpansionValve << partial >>  {
}






Class IsenthalpicExpansionValve << model >>  {
}






enum     CalcProc << type >> {
}





package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class ConstantFlowCoefficient << model >>  {
}
}






 Class PartialTwoPort << partial >>  {
}








 Class PartialTwoPortTransport << partial >>  {
}







interface FluidPort << connector >>  {
}





interface FluidPort_a << connector >>  {
}






interface FluidPort_b << connector >>  {
}

 

Modelica.Media.R134a.R134a_ph <|..-up "Medium"PartialFlowCoefficient


CalcProc -down--* "calcProc"PartialExpansionValve


ConstantFlowCoefficient <|..-up "FlowCoefficient"PartialExpansionValve


PartialTwoPortTransport <|---up PartialExpansionValve


RealInput -down--* "manVarVal"PartialExpansionValve


RealOutput -down--* "curManVarVal"PartialExpansionValve


Filter -down--* "filterOpening"PartialExpansionValve


RealPassThrough -down--* "openingThrough"PartialExpansionValve


PartialExpansionValve <|---up PartialIsenthalpicExpansionValve


PartialIsenthalpicExpansionValve <|---up IsenthalpicExpansionValve


PartialFlowCoefficient <|---up ConstantFlowCoefficient


Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"PartialTwoPort


FluidPort_a -down--* "port_a"PartialTwoPort


FluidPort_b -down--* "port_b"PartialTwoPort


PartialTwoPort <|---up PartialTwoPortTransport


Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"FluidPort


FluidPort <|---up FluidPort_a


FluidPort <|---up FluidPort_b


 @enduml
