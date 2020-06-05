@startuml




 Class PartialTwoPort << partial >>  {
 + parameter Boolean allowFlowReversal = true 
}

Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"PartialTwoPort

FluidPort_a -down--* "port_a"PartialTwoPort

FluidPort_b -down--* "port_b"PartialTwoPort
@enduml