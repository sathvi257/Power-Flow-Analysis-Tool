import numpy as np
import pandas as pd

def usage_instructions():
    """Prints usage instructions for the load flow analysis tool."""
    print("Load Flow Analysis Tool using Newton-Raphson Method")
    print("------------------------------------------------------")
    print("This tool performs load flow analysis for small power systems.")
    print("\n   Bus data format: BusID, Active Power (P), Reactive Power (Q), Voltage (V), Angle (Theta)")
    print("     1,0.0,0.0,1.0,0.0")
    print("     2,0.5,0.2,1.0,0.0")
    print("     3,0.2,0.1,1.0,0.0")
    print("\n   Line data format: FromBusID, ToBusID, Resistance (R), Reactance (X)")
    print("     1,2,0.01,0.1")
    print("     2,3,0.01,0.1")
    print("     1,3,0.01,0.1")
   

def validate_results(voltage, power_mismatch, power_losses, current_flows):
    """Validates the results of the load flow analysis."""
    assert len(voltage) > 0, "Voltage calculation failed. No voltages found."
    assert len(power_mismatch) > 0, "Power mismatch calculation failed. No mismatches found."
    assert len(power_losses) > 0, "Power loss calculation failed. No losses found."
    assert len(current_flows) > 0, "Current flow calculation failed. No currents found."
    print("\n Results \n")
