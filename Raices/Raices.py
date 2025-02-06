from scipy import optimize  

# Define the polynomial coefficients (highest power first)  
coefficients = [1, -6, 2, 20, -27, 10]  

# Define the polynomial function
def poly_func(x):
    return sum(c * x**i for i, c in enumerate(reversed(coefficients)))

# Initial guesses for the Newton method
initial_guesses = [-2, 0.5, 1, 5.5]

# Find the roots using the Newton method
roots = [optimize.newton(poly_func, guess, tol=1e-6, maxiter=500) for guess in initial_guesses]

# Sort the roots in ascending order
roots.sort()

# Remove duplicates and round to 2 decimal places
unique_roots = sorted(set(round(root, 2) for root in roots))

# Print the roots without numpy float type
print([float(root) for root in unique_roots])
