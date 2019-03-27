@startuml




 Class PartialTwoPort << partial >>  {
}

Modelica.Media.Interfaces.PartialMedium <|..-up "Medium"PartialTwoPort

FluidPort_a -down--* "port_a"PartialTwoPort

FluidPort_b -down--* "port_b"PartialTwoPort
@enduml