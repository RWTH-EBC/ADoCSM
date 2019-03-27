@startuml




 Class PartialExpansionValve << partial >>  {
}

CalcProc -down--* "calcProc"PartialExpansionValve

ConstantFlowCoefficient <|..-up "FlowCoefficient"PartialExpansionValve

PartialTwoPortTransport <|---up PartialExpansionValve

RealInput -down--* "manVarVal"PartialExpansionValve

RealOutput -down--* "curManVarVal"PartialExpansionValve

Filter -down--* "filterOpening"PartialExpansionValve

RealPassThrough -down--* "openingThrough"PartialExpansionValve
@enduml