@startuml




 Class PartialExpansionValve << partial >>  {
 + parameter Modelica.SIunits.Area AVal = 2.5e-6 
 + parameter Modelica.SIunits.Diameter dInlPip = 7.5e-3 
 + parameter Boolean useInpFil = true 
 + parameter Modelica.SIunits.Time risTim = 0.5 
 + parameter Utilities.Types.CalcProc calcProc=Utilities.Types.CalcProc.nominal 
 + parameter Modelica.SIunits.MassFlowRate mFlowNom = m_flow_nominal 
 + parameter Modelica.SIunits.PressureDifference dpNom = 15e5 
 + parameter Medium.MassFlowRate m_flow_nominal = 0.1 
 + parameter Boolean show_flow_coefficient = true 
 + parameter Boolean show_staInl = true 
 + parameter Boolean show_staOut = false 
}

CalcProc -down--* "calcProc"PartialExpansionValve

ConstantFlowCoefficient <|..-up "FlowCoefficient"PartialExpansionValve

PartialTwoPortTransport <|---up PartialExpansionValve

RealInput -down--* "manVarVal"PartialExpansionValve

RealOutput -down--* "curManVarVal"PartialExpansionValve

Filter -down--* "filterOpening"PartialExpansionValve

RealPassThrough -down--* "openingThrough"PartialExpansionValve
@enduml