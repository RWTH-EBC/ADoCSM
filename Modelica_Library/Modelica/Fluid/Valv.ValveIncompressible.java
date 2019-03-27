      end if;

    annotation (
    Documentation(info="<html>
<p>
Valve model according to the IEC 534/ISA S.75 standards for valve sizing, incompressible fluids.</p>

<p>
The parameters of this model are explained in detail in
<a href=\"modelica://Modelica.Fluid.Valves.BaseClasses.PartialValve\">PartialValve</a>
(the base model for valves).
</p>

<p>
This model assumes that the fluid has a low compressibility, which is always the case for liquids.
It can also be used with gases, provided that the pressure drop is lower than 0.2 times the absolute pressure at the inlet, so that the fluid density does not change much inside the valve.</p>

<p>
If <code>checkValve</code> is false, the valve supports reverse flow, with a symmetric flow characteristic curve. Otherwise, reverse flow is stopped (check valve behaviour).
</p>

<p>
The treatment of parameters <strong>Kv</strong> and <strong>Cv</strong> is
explained in detail in the
<a href=\"modelica://Modelica.Fluid.UsersGuide.ComponentDefinition.ValveCharacteristics\">User's Guide</a>.
</p>

</html>",
      revisions="<html>
<ul>
<li><em>2 Nov 2005</em>
    by <a href=\"mailto:francesco.casella@polimi.it\">Francesco Casella</a>:<br>
       Adapted from the ThermoPower library.</li>
</ul>
</html>"));
    end ValveIncompressible;
