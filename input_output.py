 import numpy as np

def read_bus_data(file_path):
    """Reads bus data from a specified file."""
    bus_data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            bus_id = int(parts[0])
            active_power = float(parts[1])
            reactive_power = float(parts[2])
            bus_data.append([bus_id, active_power, reactive_power])
    return bus_data

def read_line_data(file_path):
    """Reads line data from a specified file."""
    line_data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            from_bus = int(parts[0])
            to_bus = int(parts[1])
            resistance = float(parts[2])
            reactance = float(parts[3])
            line_data.append([from_bus, to_bus, resistance, reactance])
    return line_data

def display_results(voltage, power_mismatch, power_losses, current_flows):
    """Displays the results of the load flow analysis."""
    print("Bus Voltages:")
    for i, v in enumerate(voltage):
        print(f"Bus {i + 1}: {abs(v):.4f} ∠ {np.angle(v, deg=True):.2f}°")

    print("\nPower Mismatches:")
    for i, m in enumerate(power_mismatch):
        print(f"Bus {i + 1}: {m:.4f}")

    print("\nPower Losses on Lines:")
    for i, loss in enumerate(power_losses):
        print(f"Line {i + 1}: Power Loss = {loss:.4f} Watts")

    print("\nCurrent Flows on Lines:")
    for i, current in enumerate(current_flows):
        print(f"Line {i + 1}: Current Flow = {current:.4f} A")



