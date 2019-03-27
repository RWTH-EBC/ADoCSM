    end if;

    annotation (
    Documentation(info="<html>
<p>Valve model according to the IEC 534/ISA S.75 standards for valve sizing, compressible fluid, no phase change, also covering choked-flow conditions.</p>

<p>
The parameters of this model are explained in detail in
<a href=\"modelica://Modelica.Fluid.Valves.BaseClasses.PartialValve\">PartialValve</a>
(the base model for valves).
</p>

<p>This model can be used with gases and vapours, with arbitrary pressure ratio between inlet and outlet.</p>

<p>The product Fk*xt is given by the parameter <code>Fxt_full</code>, and is assumed constant by default. The relative change (per unit) of the xt coefficient with the valve opening can be specified by replacing the <code>xtCharacteristic</code> function.</p>
<p>If <code>checkValve</code> is false, the valve supports reverse flow, with a symmetric flow characteristic curve. Otherwise, reverse flow is stopped (check valve behaviour).</p>

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
  end ValveCompressible;
