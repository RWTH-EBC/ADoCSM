  model ValveDiscrete "Valve for water/steam flows with linear pressure drop"
    extends Modelica.Fluid.Interfaces.PartialTwoPortTransport;
    parameter SI.AbsolutePressure dp_nominal
      "Nominal pressure drop at full opening=1"
      annotation(Dialog(group="Nominal operating point"));
    parameter Medium.MassFlowRate m_flow_nominal
      "Nominal mass flowrate at full opening=1";
    final parameter Types.HydraulicConductance k = m_flow_nominal/dp_nominal
      "Hydraulic conductance at full opening=1";
    Modelica.Blocks.Interfaces.BooleanInput open
    annotation (Placement(transformation(
          origin={0,80},
          extent={{-20,-20},{20,20}},
          rotation=270)));
    parameter Real opening_min(min=0)=0
      "Remaining opening if closed, causing small leakage flow";
  equation
    m_flow = if open then 1*k*dp else opening_min*k*dp;

    // Isenthalpic state transformation (no storage and no loss of energy)
    port_a.h_outflow = inStream(port_b.h_outflow);
    port_b.h_outflow = inStream(port_a.h_outflow);

  annotation (
    Icon(coordinateSystem(
          preserveAspectRatio=false,
          extent={{-100,-100},{100,100}}), graphics={
          Line(points={{0,50},{0,0}}),
          Rectangle(
            extent={{-20,60},{20,50}},
            fillPattern=FillPattern.Solid),
          Polygon(
            points={{-100,50},{100,-50},{100,50},{0,0},{-100,-50},{-100,50}},
            fillColor=DynamicSelect({255,255,255}, if open > 0.5 then {0,255,0} else
