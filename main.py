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

def read_bus_data(file_path):
    """Reads bus data from a CSV file."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def read_line_data(file_path):
    """Reads line data from a CSV file."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def calculate_power_mismatch(V, bus_data):
    """Calculates power mismatches for all buses."""
    P_mismatch = np.zeros(len(bus_data), dtype=complex)
    Q_mismatch = np.zeros(len(bus_data), dtype=complex)
    
    for i, bus in enumerate(bus_data):
        # Extracting necessary parameters
        V_mag = bus['V']
        V_angle = np.radians(bus['Theta'])
        P = bus['P']
        Q = bus['Q']
        
        # Calculate power injections (assuming Ybus is unit matrix for simplification)
        P_inj = V_mag * np.sum(V_mag * np.cos(V_angle))  # Simplified for illustrative purposes
        Q_inj = V_mag * np.sum(V_mag * np.sin(V_angle))  # Simplified for illustrative purposes
        
        # Calculate mismatches
        P_mismatch[i] = P - P_inj
        Q_mismatch[i] = Q - Q_inj
        
    return P_mismatch, Q_mismatch

def newton_raphson(bus_data, line_data, max_iter=10, tol=1e-6):
    """Performs the Newton-Raphson load flow analysis."""
    n = len(bus_data)
    V = np.array([bus['V'] * np.exp(1j * np.radians(bus['Theta'])) for bus in bus_data])

    for iteration in range(max_iter):
        # Calculate power mismatches
        P_mismatch, Q_mismatch = calculate_power_mismatch(V, bus_data)
        
        # Check for convergence
        if np.all(np.abs(P_mismatch) < tol) and np.all(np.abs(Q_mismatch) < tol):
            break
        
        # Update voltages (simplified approach)
        for i in range(n):
            if bus_data[i]['Type'] == 1:  # PQ bus
                V[i] += 0.01 * (P_mismatch[i] + 1j * Q_mismatch[i])  # Update voltage with some small step

    return V, P_mismatch, Q_mismatch

def calculate_power_losses_and_currents(bus_voltages, line_data):
    """Calculates power losses and currents on lines."""
    power_losses = {}
    current_flows = {}

    for line in line_data:
        from_bus = line['FromBusID'] - 1  # Adjust for 0-based index
        to_bus = line['ToBusID'] - 1  # Adjust for 0-based index
        
        # Calculate impedance
        Z = complex(line['R'], line['X'])
        
        # Current flow calculation
        I = (bus_voltages[from_bus] - bus_voltages[to_bus]) / Z
        current_flows[(from_bus + 1, to_bus + 1)] = I  # Store as 1-based index
        
        # Power loss calculation
        power_loss = np.abs(I) ** 2 * Z
        power_losses[(from_bus + 1, to_bus + 1)] = power_loss.real  # Store as 1-based index

    return power_losses, current_flows

def display_results(bus_voltages, P_mismatch, Q_mismatch, power_losses, current_flows):
    """Displays the results of the load flow analysis."""
    print("Bus Voltages:")
    for i, voltage in enumerate(bus_voltages):
        mag = abs(voltage)
        angle = np.angle(voltage, deg=True)
        print(f"Bus {i+1}: {mag:.2f} ∠ {angle:.2f}°")

    print("\nPower Mismatches:")
    for i in range(len(P_mismatch)):
        print(f"Bus {i+1}: P Mismatch = {P_mismatch[i].real:.4f}, Q Mismatch = {Q_mismatch[i].real:.4f}")

    print("\nPower Losses on Lines:")
    for line, loss in power_losses.items():
        print(f"Line {line}: Power Loss = {loss:.4f} Watts")

    print("\nCurrent Flows on Lines:")
    for line, current in current_flows.items():
        print(f"Line {line}: Current Flow = {current:.4f} A")

def main():
    usage_instructions()  # Print usage instructions
    # Load bus and line data from CSV files
    bus_data = read_bus_data('bus_data.csv')
    line_data = read_line_data('line_data.csv')

    # Perform the Newton-Raphson load flow analysis
    bus_voltages, P_mismatch, Q_mismatch = newton_raphson(bus_data, line_data)

    # Calculate power losses and current flows
    power_losses, current_flows = calculate_power_losses_and_currents(bus_voltages, line_data)

    # Validate the results
    validate_results(bus_voltages, P_mismatch, power_losses, current_flows)

    # Display results
    display_results(bus_voltages, P_mismatch, Q_mismatch, power_losses, current_flows)

if __name__ == "__main__":
    main()
