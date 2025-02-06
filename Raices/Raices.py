import numpy as np  
from scipy import optimize  

# Define the polynomial coefficients (highest power first)  
coefficients = [1, -6, 2, 20, -27, 10]  

# Find the roots of the polynomial  
roots = optimize.newton(lambda x: np.polyval(coefficients, x), np.array([-2, 0.5, 1, 5.5]), tol = 1e-6, maxiter = 500)  
# Sort the roots in ascending order  
roots.sort()  
unique_roots = np.unique(roots.round(decimals=2))  

# Print the roots  
print(unique_roots)
 








