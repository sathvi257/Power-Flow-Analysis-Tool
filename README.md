# Power-Flow-Analysis-Tool
A Python-based command-line tool for performing power system load flow analysis using the Gauss-Seidel and Newton-Raphson methods. It calculates bus voltages, power losses, and current flows for small power systems. Includes input/output functionality and test cases for validation.

# Load Flow Analysis Tool

## Overview
The **Load Flow Analysis Tool** is a Python-based application designed to perform load flow analysis for small power systems using the **Newton-Raphson method**. This tool facilitates the calculation of critical parameters such as bus voltages, power losses, and current flows, making it a valuable asset for power system engineers and researchers.

## Team Members
- **SWATI IPPALLI**: Responsible for implementing the mathematical models and algorithms for the Newton-Raphson method.
- **SATVIKA LS**: Develops input/output functions for handling bus and line data.
- **OBULAKSHMI P O**: Compiles comprehensive usage instructions and validates the tool's results with sample inputs.

## Features
- **Bus Voltage Calculation**: Accurately determines voltage levels at various buses within the power system.
- **Power Loss Calculation**: Evaluates power losses in transmission lines due to resistance.
- **Current Flow Evaluation**: Computes current flowing through each transmission line in the network.
- **User-Friendly Interface**: Operates via the command line, with clear input and output formatting.

## Program Flow
The program follows a structured flow to perform load flow analysis effectively:

1. **Initialization**:
   - Load necessary libraries and modules.
   - Initialize data structures to store bus and line information.

2. **Input Handling**:
   - Use functions to gather input data for:
     - Number of buses in the system.
     - Parameters for each bus (e.g., bus type, power injections).
     - Transmission line data (e.g., impedance, admittance).

3. **Mathematical Modeling**:
   - Implement the Newton-Raphson method to establish the power flow equations:
     - Formulate equations for active and reactive power.
     - Derive the Jacobian matrix required for iterative solutions.

4. **Iteration Process**:
   - Use the Newton-Raphson iterative method to update bus voltages and angles until convergence is achieved:
     - Calculate power mismatches.
     - Update voltage estimates based on the Jacobian matrix.

5. **Output Calculation**:
   - Once convergence is reached, calculate the final bus voltages, power losses, and current flows.

6. **Display Results**:
   - Format and present the results to the user, showing:
     - Bus voltages.
     - Total power losses in the system.
     - Current flow in each line.

7. **Documentation**:
   - Provide comprehensive documentation, including usage instructions, examples, and validation results.

## Usage
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/load-flow-analysis-tool.git
   ```
2. Navigate to the project directory and install any required dependencies.

### Running the Tool
Execute the main script from the command line:
```bash
python load_flow_analysis.py
```

### Input Format
Input data should be provided as specified in the documentation, including:
- Bus information (number, type, power injections).
- Transmission line data (impedance, admittance).

### Output
The tool will display:
- Calculated bus voltages.
- Total power losses in the system.
- Current flowing through each line.

## Documentation
Comprehensive usage instructions and validated test cases are included in the documentation to guide users on how to effectively use the tool.

## Future Work
Future enhancements may include:
- Development of a graphical user interface (GUI) for improved user experience.
- Extension of the tool to accommodate larger power systems.
- Integration of additional features such as contingency analysis and optimization techniques.
