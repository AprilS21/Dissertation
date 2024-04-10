import sys
import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve
import numpy as np

def hex_to_int(hex_key):
    return int(hex_key, 16)

def plot_hilbert_curve(coordinates):
    """
    Plot Hilbert Curve of a set of coordinates

    Parameters:
    coordinates (generator) : generator yielding coordinates as (x, y) tuples
    """
    plt.figure(figsize=(8, 8))
    plt.title("Hilbert Curve")
    x, y = zip(*coordinates)
    plt.plot(x, y, color='blue', marker='o')
    plt.gca().invert_yaxis()  # Invert y-axis
    plt.savefig('./hilbertCurve.png')

def generate_coordinates(file_path):
    with open(file_path, 'r') as file:
        for line_count, line in enumerate(file, start=1):
            line = line.strip()
            if len(line) != 32:
                print(f"Skipping bad length line at line {line_count}: {line}", file=sys.stderr)
                continue
            int_value = hex_to_int(line)
            yield int_value

def main(path):
    line_count = 0
    with open(path, 'r') as file:
        for _ in file:
            line_count += 1

    print("Total number of keys:", line_count)

    side_length = int(np.ceil(np.sqrt(line_count)))
    p = int(np.ceil(np.log2(side_length)))
    hilbert_curve = HilbertCurve(p, 2)

    coordinates = (hilbert_curve.point_from_distance(i) for i in generate_coordinates(path))
    plot_hilbert_curve(coordinates)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hilbertCurve.py input_file_path")
        sys.exit(1)
    path = sys.argv[1]
    main(path)
