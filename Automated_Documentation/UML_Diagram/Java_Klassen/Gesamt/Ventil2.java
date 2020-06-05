@startuml{




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












 Class PartialIsenthalpicExpansionValve << partial >>  {
}






Class IsenthalpicExpansionValve << model >>  {
}






enum	 CalcProc << type >> {
}





Class PolynomialFlowCoefficient << model >>  {
 + parameter Types.PolynomialModels polyMod=Types.PolynomialModels.ShanweiEtAl2005 
 + parameter Real a [ : ]  
 + parameter Real b [ : ]  
 + parameter Integer nT = size  {  a,1  }   
 + parameter Modelica.SIunits.Diameter dCle = 0.02e-3 
 + parameter Real pDifRat = 0.84 
}






Class PowerFlowCoefficient << model >>  {
 + parameter Types.PowerModels powMod=Types.PowerModels.ShanweiEtAl2005 
 + parameter Real a 
 + parameter Real b [ : ]  
 + parameter Integer nT = size  {  b,1  }   
 + parameter Modelica.SIunits.Diameter dCle = 0.02e-3 
 + parameter Real pDifRat = 0.84 
}




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class Buck_R22R407CR410A_EEV_15_22 << model >>  {
}
}




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class Buck_R22R407CR410A_EEV_16_18 << model >>  {
}
}






package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class ConstantFlowCoefficient << model >>  {
 + parameter Real C_const  {  unit="1", min = 0, max = 100, nominal = 25  }   = 15 
}
}




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class Poly_R22R407CR410A_EEV_15_22 << model >>  {
}
}




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class Poly_R22_EEV_16 << model >>  {
}
}




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class Poly_R407c_EEV_18 << model >>  {
}
}




package Utilities.FlowCoefficient.SpecifiedFlowCoefficients{ 

Class Power_R134a_EEV_15 << model >>  {
}
}






 Class PartialTwoPort << partial >>  {
 + parameter Boolean allowFlowReversal = true 
}








 Class PartialTwoPortTransport << partial >>  {
 + parameter Modelica.SIunits.PressureDifference dp_start  {  displayUnit="Pa"  }   = 0 
 + parameter Medium.MassFlowRate m_flow_start = 0 
 + parameter Medium.MassFlowRate m_flow_small 
 + parameter Boolean show_T = true 
 + parameter Boolean show_V_flow = true 
}






interface FluidPort_a << connector >>  {
}






interface FluidPort_b << connector >>  {
}

 

CalcProc -down--* "calcProc"PartialExpansionValve


ConstantFlowCoefficient <|..-up "FlowCoefficient"PartialExpansionValve


PartialTwoPortTransport <|---up PartialExpansionValve


RealInput -down--* "manVarVal"PartialExpansionValve


RealOutput -down--* "curManVarVal"PartialExpansionValve


Filter -down--* "filterOpening"PartialExpansionValve


RealPassThrough -down--* "openingThrough"PartialExpansionValve


PartialExpansionValve <|---up PartialIsenthalpicExpansionValve


PartialIsenthalpicExpansionValve <|---up IsenthalpicExpansionValve


PartialFlowCoefficient <|---up PolynomialFlowCoefficient


PartialFlowCoefficient <|---up PowerFlowCoefficient


PowerFlowCoefficient <|---up Buck_R22R407CR410A_EEV_15_22


PowerFlowCoefficient <|---up Buck_R22R407CR410A_EEV_16_18


PartialFlowCoefficient <|---up ConstantFlowCoefficient


PolynomialFlowCoefficient <|---up Poly_R22R407CR410A_EEV_15_22


PolynomialFlowCoefficient <|---up Poly_R22_EEV_16


PolynomialFlowCoefficient <|---up Poly_R407c_EEV_18


PowerFlowCoefficient <|---up Power_R134a_EEV_15


Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"PartialTwoPort


FluidPort_a -down--* "port_a"PartialTwoPort


FluidPort_b -down--* "port_b"PartialTwoPort


PartialTwoPort <|---up PartialTwoPortTransport


FluidPort <|---up FluidPort_a


FluidPort <|---up FluidPort_b


 @enduml
