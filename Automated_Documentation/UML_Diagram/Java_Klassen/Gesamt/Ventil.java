@startuml




 Class PartialFlowCoefficient << partial >>  {
}

Modelica.Media.R134a.R134a_ph <|..-up "Medium"PartialFlowCoefficient





 Class PartialExpansionValve << partial >>  {
}

CalcProc -down--* "calcProc"PartialExpansionValve

ConstantFlowCoefficient <|..-up "FlowCoefficient"PartialExpansionValve

PartialTwoPortTransport <|---up PartialExpansionValve

RealInput -down--* "manVarVal"PartialExpansionValve

RealOutput -down--* "curManVarVal"PartialExpansionValve

Filter -down--* "filterOpening"PartialExpansionValve

RealPassThrough -down--* "openingThrough"PartialExpansionValve





 Class PartialIsenthalpicExpansionValve << partial >>  {
}

PartialExpansionValve <|---up PartialIsenthalpicExpansionValve





Class IsenthalpicExpansionValve << model >>  {
}

PartialIsenthalpicExpansionValve <|---up IsenthalpicExpansionValve





enum     CalcProc << type >> {
}





package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class ConstantFlowCoefficient << model >>  {
}
}

PartialFlowCoefficient <|---up ConstantFlowCoefficient





 Class PartialTwoPort << partial >>  {
}

Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"PartialTwoPort

FluidPort_a -down--* "port_a"PartialTwoPort

FluidPort_b -down--* "port_b"PartialTwoPort





 Class PartialTwoPortTransport << partial >>  {
}

PartialTwoPort <|---up PartialTwoPortTransport


Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"FluidPort




interface FluidPort << connector >>  {
}





interface FluidPort_a << connector >>  {
}

FluidPort <|---up FluidPort_a





interface FluidPort_b << connector >>  {
}

FluidPort <|---up FluidPort_b
 
 @enduml