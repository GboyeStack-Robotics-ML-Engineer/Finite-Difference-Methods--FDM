
# 2D Steady-State Temperature Distribution Solver

This repository contains a Python implementation of a **Finite Difference Method (FDM)** to solve for the steady-state temperature distribution in a 2D domain. The project applies numerical methods to simulate heat conduction under given boundary conditions and visualize the results.

## Features
- **Flexible Boundary Conditions**: Specify temperature values for the top, bottom, left, and right edges.
- **Efficient Coefficient Matrix Assembly**: Utilizes block diagonal matrices for optimized computation.
- **Interactive Visualization**: Generates a heat map of the temperature distribution.
- **Customizable Grid**: Set the grid resolution with the number of points along the x and y axes.

## Dependencies
- Python 3.7+
- NumPy
- Matplotlib
- SciPy


## Usage
Clone the repository using git:
```bash
git clone https://github.com/GboyeStack-Robotics-ML-Engineer/Finite-Difference-Methods--FDM-.git
```
Navigate to the project directory:
```bash
cd Finite-Difference-Methods--FDM
```
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

Run the script with the following command:
```bash
python -m 2d_Solver_steadyFlow.py --Nx <Nx> --Ny <Ny> --Bc <boundary_conditions> --plot <True/False>
```

### Parameters
- `--Nx`: Number of grid points in the x-direction (integer).
- `--Ny`: Number of grid points in the y-direction (integer).
- `--Bc`: Boundary conditions, provided as key-value pairs:
  - `top=<value>`
  - `bottom=<value>`
  - `left=<value>`
  - `right=<value>`
- `--plot`: Boolean flag to visualize the temperature distribution (`True` or `False`).

### Example
```bash
python 2d_Solver_steadyFlow.py --Nx 100 --Ny 100 --Bc top=10 bottom=0 left=0 right=0 --plot True
```

## How It Works
1. **Matrix Assembly**: The solver constructs a sparse coefficient matrix representing the finite difference approximation of the Laplace equation.
2. **Boundary Conditions**: Boundary values are applied to the edges of the 2D domain.
3. **Solution**: Solves the linear system to compute temperature values at internal nodes.
4. **Visualization**: Displays the temperature distribution using a heat map.

## Output
- **Textual Solution**: A matrix representing the computed temperatures at all nodes.
- **Heat Map**: A visual representation of the temperature distribution.

![image](https://github.com/user-attachments/assets/65156c63-645d-4b3b-97ad-3408e9fa44cb)

## Project Structure
- `2d_Solver_steadyFlow.py`: Main Python script containing the solver and plotting functionalities.

## Contributing
Contributions are welcome! Feel free to fork the repository, submit issues, or make pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the open-source Python community for providing the tools necessary for numerical simulations and data visualization.
