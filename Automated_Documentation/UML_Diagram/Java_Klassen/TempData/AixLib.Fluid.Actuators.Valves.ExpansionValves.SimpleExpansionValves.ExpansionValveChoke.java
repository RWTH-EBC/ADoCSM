
within AixLib.Fluid.Actuators.Valves.ExpansionValves.SimpleExpansionValves;
model ExpansionValveChoke "Model with choke conditions"
extends BaseClasses.PartialIsenthalpicExpansionValve
Real X =  ( pInl - pOut ) /pInl "Ratio of pressure differential to inlet absolute pressure";
Real Y = 1 - X/ ( 3*F_y*X_T )  "Expansion factor";
Real F_y = kappa/1.4 "Specfic haet ratio factor";
Real kappa "specific heat for the fluid through valve";
Real F_F "Liquid critical pressure ratio factor";
Medium.SaturationProperties satInl "Saturation properties at valve's inlet conditions";
Real F_l  =  0.7 "Liquid pressure recovery factor for a control valve without attached fittings";
parameter Real X_T = 0.7 "pressure differential ratio factor of a controlled valve";
equation
satInl  =  Medium.setSat_T ( Medium.temperature ( staInl )  )  "Saturtation properties"

F_F*Medium.fluidConstants[1].criticalPressure  =  0.96*Medium.fluidConstants[1].criticalPressure - 0.28* ( satInl.psat )  "Liquid critical pressure ratio factor";
kappa*Medium.specificHeatCapacityCv ( staInl )  =  Medium.specificHeatCapacityCp ( staInl )  "Isentrop exponent";
C  =  0.95;
if staInl.phase  =  =  1 and staOut.phase  =  =  1 then m_flow^2  =  C^2*AThr^2*2*Medium.density ( staInl ) * ( pInl - pOut ) ;
elseif X < F_y*X_T then m_flow^2  =  C^2*AThr^2*Y^2* ( 2*Medium.density ( staInl ) *pInl*X ) ;
elseif X > =  F_y*X_T then m_flow^2  =  C^2*AThr^2* ( 2/3 ) ^2* ( 2*Medium.density ( staInl ) *pInl*X_T*F_y ) ;
else m_flow^2  =  0;
end if;
annotation  ( Icon ( coordinateSystem ( preserveAspectRatio = false )  ) , Diagram (  coordinateSystem ( preserveAspectRatio = false )  )  ) ;
end ExpansionValveChoke;