@startuml




 Class PartialCompressor << partial >>  {
 + pre(isOn) (if y > 0.01 then true else fals)
 + assert ( port_b.T > ref.T_min and port_b.T < ref.TCri, "Condensing temperature must be above the minimum refrigerant temperature and below the critical temperature." )
 + assert ( port_a.T > ref.T_min and port_a.T < ref.TCri, "Evaporating temperature must be above the minimum refrigerant temperature and below the critical temperature." )
 + isOn (not pre(isOn) and y > 0.01 or pre(isOn) and y >= 0.00)
 + PR (max(pDis/pSuc, 0))
 + vSuc (ref.specificVolumeVap_pT(pSuc, TSuc))
 + pCon (ref.pressureSatVap_T(port_b.T))
 + hCon (ref.enthalpySatLiq_T(port_b.T))
 + pEva (ref.pressureSatVap_T(port_a.T))
 + hEva (ref.enthalpySatVap_T(port_a.T))
}

AixLib.Media.Refrigerants.R410A <|.. "ref"PartialCompressor

HeatPort_a *-- "port_a"PartialCompressor

HeatPort_b *-- "port_b"PartialCompressor

RealInput *-- "y"PartialCompressor

RealOutput *-- "P"PartialCompressor





Class ReciprocatingCompressor << model >>  {
 + (if isOn then pSuc = AixLib.Utilities.Math.Functions.smoothMin(pEva - pDro, pCon - pDro, 0.01*ref.pCri) ; pDis = pCon + pDro ; k = ref.isentropicExponentVap_Tv(TSuc, vSuc) ; m_flow = pisDis_norm*pisDis/vSuc*(1 + cleFac - cleFac* ( PR)^ ( 1/k)) ; PThe = k/(k-1) * m_flow*pSuc*vSuc*((PR)^((k-1)/k)-1) ; P = PThe/etaEle + PLos ; TSuc = port_a.T + dTSup ; port_a.Q_flow = m_flow * (hEva - hCon) ; port_b.Q_flow = - (port_a.Q_flow + P) ; -port_b.Q_flow = P * COP ; pSuc = pEva ; pDis = pCon ; m_flow = 0 ; PThe = 0 ; P = 0 ; TSuc = port_a.T ; port_a.Q_flow = 0 ; port_b.Q_flow = 0 ; COP = 1.0 ; end if ; )
 + (else k = 1.0 ;;pSuc = pEva ;;pDis = pCon ;;m_flow = 0 ;;PThe = 0 ;;P = 0 ;;TSuc = port_a.T ;;port_a.Q_flow = 0 ;;port_b.Q_flow = 0 ;;COP = 1.0 ;;)
 + (end if ;)
 + pisDis_norm (AixLib.Utilities.Math.Functions.smoothLimit(y, 0.0, 1.0, 0.001)
}

PartialCompressor <|-- ReciprocatingCompressor


Record <|-- HeatPumps




 Class HeatPumps << partial >>  {
}





 Class HeatPort << partial >>  {
}





interface HeatPort_a << connector >>  {
}

HeatPort <|-- HeatPort_a





interface HeatPort_b << connector >>  {
}

HeatPort <|-- HeatPort_b
 
 @enduml