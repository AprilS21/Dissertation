import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve
import numpy as np

def hex_to_int(hex_key):
    return int(hex_key, 16)

def plot_hilbert_curve(hex_keys):
    int_values = list(map(hex_to_int, hex_keys))

    # Calculate the side length of the square to fit all points
    side_length = int(np.ceil(np.sqrt(len(int_values))))

    # Create a Hilbert curve
    p = int(np.ceil(np.log2(side_length)))
    hilbert_curve = HilbertCurve(p, 2)

    # Get Hilbert curve coordinates for integer values
    coordinates = [hilbert_curve.point_from_distance(x) for x in range(len(int_values))]

    # Plot the points on the Hilbert curve
    plt.figure(figsize=(8, 8))
    plt.title("Hilbert Curve")
    plt.plot(*zip(*coordinates), color='blue', marker='o')
    plt.gca().invert_yaxis()  # Invert y-axis to match Hilbert curve orientation
    plt.savefig('hilbertCurve.png')


file_name = "sampleData/snippetTeks"
with open(file_name, 'r') as file:
        hex_keys = file.readlines()

plot_hilbert_curve(hex_keys)
