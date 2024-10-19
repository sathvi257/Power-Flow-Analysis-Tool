import numpy as np

def newton_raphson(bus_data, line_data, max_iter=100, tolerance=1e-6):
    num_buses = len(bus_data)
    voltage = np.ones(num_buses, dtype=complex)  # Initial bus voltages
    power_mismatch = np.zeros(num_buses, dtype=complex)

    for iteration in range(max_iter):
        power_mismatch = calculate_power_mismatch(bus_data, voltage, line_data)

        if np.all(np.abs(power_mismatch) < tolerance):
            break

        jacobian = build_jacobian(bus_data, voltage, line_data)
        voltage_update = np.linalg.solve(jacobian, -power_mismatch)
        voltage += voltage_update

    power_losses, current_flows = calculate_losses_and_currents(voltage, line_data)

    return voltage, power_mismatch, power_losses, current_flows

def calculate_power_mismatch(bus_data, voltage, line_data):
    mismatch = np.zeros(len(bus_data), dtype=complex)

    for i, bus in enumerate(bus_data):
        P = bus[1]  # Active power
        Q = bus[2]  # Reactive power
        S = voltage[i] * np.conj(P + 1j * Q)
        mismatch[i] = P - S.real + 1j * (Q - S.imag)

    return mismatch

def build_jacobian(bus_data, voltage, line_data):
    num_buses = len(bus_data)
    jacobian = np.zeros((2*num_buses, 2*num_buses), dtype=complex)

    for i in range(num_buses):
        jacobian[i, i] = 1  # Placeholder for simplification

    # More detailed Jacobian computation can be added here

    return jacobian

def calculate_losses_and_currents(voltage, line_data):
    power_losses = []
    current_flows = []

    for line in line_data:
        from_bus = line[0] - 1  # Adjust for 0-indexing
        to_bus = line[1] - 1
        resistance = line[2]
        reactance = line[3]

        current = (voltage[from_bus] - voltage[to_bus]) / (resistance + 1j * reactance)
        power_flow = voltage[from_bus] * np.conj(current)

        power_loss = np.abs(current)**2 * resistance
        power_losses.append(power_loss)
        current_flows.append(current)

    return power_losses, current_flows
