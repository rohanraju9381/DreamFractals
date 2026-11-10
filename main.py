
import numpy as np
import matplotlib.pyplot as plt

# Image resolution
WIDTH = 1600
HEIGHT = 1200

# Calculate the Mandelbrot fractal
def calculate_fractal(xmin, xmax, ymin, ymax, max_iter):

    x = np.linspace(xmin, xmax, WIDTH)
    y = np.linspace(ymin, ymax, HEIGHT)

    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C)
    iterations = np.zeros(C.shape, dtype=int)

    escaped = np.zeros(C.shape, dtype=bool)

    for i in range(max_iter):

        active = ~escaped

        Z[active] = Z[active] ** 2 + C[active]

        newly_escaped = active & (np.abs(Z) > 2)

        iterations[newly_escaped] = i + 1

        escaped |= newly_escaped

    iterations[~escaped] = max_iter

    return iterations


# Initial viewing area
xmin, xmax = -2, 1
ymin, ymax = -1.2, 1.2

# Create the window
fig, ax = plt.subplots(figsize=(10, 7.5))

def render():

    global xmin, xmax, ymin, ymax

    # More iterations as we zoom deeper
    zoom_level = np.log2(3 / (xmax - xmin))

    max_iter = min(
    3000,
    200 + int(150 * max(0, zoom_level))
    )

    print("Calculating fractal...")
    print("Iterations:", max_iter)

    data = calculate_fractal(
        xmin, xmax, ymin, ymax, max_iter
    )

    ax.clear()

    ax.imshow(
    data,
    extent=[xmin, xmax, ymin, ymax],
    origin="lower",
    cmap="magma",
    interpolation="bilinear"
    )

    ax.set_title("DreamFractals - Interactive Mandelbrot")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")

    fig.canvas.draw_idle()


# Mouse-wheel zoom
def zoom(event):

    global xmin, xmax, ymin, ymax

    if event.inaxes != ax:
        return

    if event.xdata is None or event.ydata is None:
        return

    # Zoom in or out
    if event.button == "up":
        factor = 0.8
    else:
        factor = 1.25

    mouse_x = event.xdata
    mouse_y = event.ydata

    width = (xmax - xmin) * factor
    height = (ymax - ymin) * factor

    # Keep the mouse position as the zoom centre
    rx = (mouse_x - xmin) / (xmax - xmin)
    ry = (mouse_y - ymin) / (ymax - ymin)

    xmin = mouse_x - rx * width
    xmax = xmin + width

    ymin = mouse_y - ry * height
    ymax = ymin + height

    render()


# Connect mouse-wheel event
fig.canvas.mpl_connect("scroll_event", zoom)

# First rendering
render()

plt.show()
