import numpy as np
import csv

# Function to read bus data from CSV
def read_bus_data(file_path):
    bus_data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            bus_data.append({
                'bus_id': int(row[0]),
                'P': float(row[1]),
                'Q': float(row[2])
            })
    return bus_data

# Function to read line data from CSV
def read_line_data(file_path):
    line_data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            line_data.append({
                'from_bus': int(row[0]),
                'to_bus': int(row[1]),
                'R': float(row[2]),
                'X': float(row[3])
            })
    return line_data

# Function to calculate admittance matrix (Y-bus)
def calculate_admittance_matrix(bus_data, line_data):
    num_buses = len(bus_data)
    Y_bus = np.zeros((num_buses, num_buses), dtype=complex)
    
    for line in line_data:
        from_bus = line['from_bus'] - 1
        to_bus = line['to_bus'] - 1
        Z = complex(line['R'], line['X'])
        Y = 1 / Z
        
        Y_bus[from_bus, from_bus] += Y
        Y_bus[to_bus, to_bus] += Y
        Y_bus[from_bus, to_bus] -= Y
        Y_bus[to_bus, from_bus] -= Y

    return Y_bus

# Function to perform Newton-Raphson load flow analysis
def newton_raphson_load_flow(bus_data, Y_bus, tol=1e-6, max_iter=10):
    num_buses = len(bus_data)
    V = np.ones(num_buses, dtype=complex)  # Initial guess of bus voltages
    P = np.array([bus['P'] for bus in bus_data])
    Q = np.array([bus['Q'] for bus in bus_data])
    
    for iteration in range(max_iter):
        mismatches = np.zeros(num_buses, dtype=complex)
        
        for i in range(num_buses):
            for j in range(num_buses):
                mismatches[i] += V[i] * np.conj(Y_bus[i, j] * V[j])
            mismatches[i] = P[i] + 1j * Q[i] - mismatches[i]
        
        max_mismatch = max(abs(mismatches))
        if max_mismatch < tol:
            print(f"Converged in {iteration + 1} iterations.")
            break
        
        # Update voltages (simple approximation for demonstration)
        for i in range(num_buses):
            V[i] += mismatches[i] / Y_bus[i, i]
    
    return V, mismatches

# Main function
def main():
    print("Load Flow Analysis Tool using Newton-Raphson Method")
    print("------------------------------------------------------")
    print("This tool performs load flow analysis for small power systems.")
    
    # Read bus and line data from CSV files
    bus_data = read_bus_data('C:/Users/obula/OneDrive/Desktop/bus_data.csv')
    line_data = read_line_data('C:/Users/obula/OneDrive/Desktop/line_data.csv')
    
    # Calculate admittance matrix
    Y_bus = calculate_admittance_matrix(bus_data, line_data)
    
    # Perform load flow analysis
    V, mismatches = newton_raphson_load_flow(bus_data, Y_bus)
    
    # Output the results
    print("\nBus Voltages:")
    for i, v in enumerate(V):
        print(f"Bus {i + 1}: {v} ∠ {np.angle(v, deg=True):.2f}°")
    
    print("\nPower Mismatches:")
    for i, mismatch in enumerate(mismatches):
        print(f"Bus {i + 1}: {mismatch}")
    
    # Calculate power losses and current flows (simplified for demonstration)
    print("\nPower Losses on Lines:")
    for i, line in enumerate(line_data):
        from_bus = line['from_bus'] - 1
        to_bus = line['to_bus'] - 1
        current = (V[from_bus] - V[to_bus]) / complex(line['R'], line['X'])
        power_loss = abs(current)**2 * line['R']
        print(f"Line {i + 1}: Power Loss = {power_loss:.4f} Watts")
    
    print("\nCurrent Flows on Lines:")
    for i, line in enumerate(line_data):
        from_bus = line['from_bus'] - 1
        to_bus = line['to_bus'] - 1
        current = (V[from_bus] - V[to_bus]) / complex(line['R'], line['X'])
        print(f"Line {i + 1}: Current Flow = {current} A")

if __name__ == "__main__":
    main()

