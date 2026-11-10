
import numpy as np
import matplotlib.pyplot as plt

# Create a grid of complex numbers
width = 800
height = 600

x = np.linspace(-2, 1, width)
y = np.linspace(-1.2, 1.2, height)

X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# Start with z = 0
Z = np.zeros_like(C)

# Count iterations
iterations = np.zeros(C.shape, dtype=int)

# Generate Mandelbrot fractal
for i in range(100):
    Z = Z**2 + C
    mask = np.abs(Z) < 2
    iterations[mask] = i

# Display the fractal
plt.figure(figsize=(12, 8))
plt.imshow(iterations, cmap="inferno", extent=[-2, 1, -1.2, 1.2])
plt.colorbar(label="Iterations")
plt.title("DreamFractals - Mandelbrot Set")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.show()
