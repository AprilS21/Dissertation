import sys
import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve
import numpy as np

def hex_to_int(hex_key):
    return int(hex_key, 16)

def plot_hilbert_curve(hex_keys):
    """
    Plot Hilbert Curve of a set of keys

    Parameters:
    hex_keys (list[str]) : list of hexadecimal keys

    Returns:
    Saves plot as hilbertCurve.png
    """
    int_values = list(map(hex_to_int, hex_keys))
    side_length = int(np.ceil(np.sqrt(len(int_values))))

    # Create curve
    p = int(np.ceil(np.log2(side_length)))
    hilbert_curve = HilbertCurve(p, 2)

    # get coordinates
    coordinates = [hilbert_curve.point_from_distance(x) for x in range(len(int_values))]

    plt.figure(figsize=(12, 12))
    plt.title("Hilbert Curve")
    plt.plot(*zip(*coordinates), color='blue', marker='o')
    plt.gca().invert_yaxis()  # Invert y-axis
    plt.savefig('./hilbertCurve.png')

def main(path):
    hex_keys = []
    line_count =0
    with open(path, 'r') as file:
        for line in file:
            if (len(line) != 33):
                line_count += 1
                print("Skipping bad length line at",line_count,"line:",line,file=sys.stderr)
                print("length",len(line),file=sys.stderr)
                continue
            try:
                hex_keys.append(line)
                line_count += 1
            except Exception as e:
                print("Exception",e,"at",line_count,file=sys.stderr)
                print("Line:",line,file=sys.stderr)
        
    plot_hilbert_curve(hex_keys)

if __name__ == "__main__":
    path = str(sys.argv[1])
    main(path)