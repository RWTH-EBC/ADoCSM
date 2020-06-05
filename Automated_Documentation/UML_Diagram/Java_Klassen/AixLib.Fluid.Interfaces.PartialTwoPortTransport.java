@startuml




 Class PartialTwoPortTransport << partial >>  {
 + parameter Modelica.SIunits.PressureDifference dp_start  {  displayUnit="Pa"  }   = 0 
 + parameter Medium.MassFlowRate m_flow_start = 0 
 + parameter Medium.MassFlowRate m_flow_small 
 + parameter Boolean show_T = true 
 + parameter Boolean show_V_flow = true 
}

PartialTwoPort <|---up PartialTwoPortTransport
@enduml