#file:///C:/Program%20Files/Dymola%202019/Modelica/Library/python_interface/doc/index.html

import os
# Import dymola package
from dymola.dymola_interface import DymolaInterface

# Start the interface
dymola = DymolaInterface()

# Location of your local AixLib clone
dir_aixlib = r"C:\Users\hinack\Dropbox\09_Modelica_Library\AixLib"
# Location where to store the results
dir_result = r"C:\Users\hinack\Dropbox\18_ModelManagement"

# Open AixLib
dymola.openModel(path=os.path.join(dir_aixlib, 'package.mo'))

# Translate any model you'd like to simulate
dymola.translateModel('AixLib.ThermalZones.ReducedOrder.Examples.ThermalZone')

# Simulate the model
output = dymola.simulateExtendedModel(
    problem='AixLib.ThermalZones.ReducedOrder.Examples.ThermalZone',
    startTime=0.0,
    stopTime=3.1536e+07,
    outputInterval=3600,
    method="Dassl",
    tolerance=0.0001,
    resultFile=os.path.join(dir_result, 'demo_results'),
    finalNames=['thermalZone.TAir' ],
)

dymola.close()