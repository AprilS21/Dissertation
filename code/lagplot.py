import sys
import matplotlib.pyplot as plt 

def main(path):
    """
    Creates lag plot for set of keys

    Parameters:
    path to file containing keys, binary format

    Returns:
    saves figure as lagplot.png
    """
    lag = 1
    with open(path, 'r') as file:
        # Initialize variables to store current and previous values
        prev_value = None
        prev_index = None
        
        # Iterate over each line in the file
        for line_count, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            value = int(line)
            
            # Plot lag plot
            if prev_value is not None:
                plt.scatter(prev_value, value, color='blue', marker='o', alpha=0.5)
            prev_value = value

    # Add labels and title
    plt.xlabel(f'x(t)')
    plt.ylabel(f'x(t + {lag})')
    plt.title(f'Lag Plot (lag={lag})')

    # Save the plot
    plt.savefig('./lagplot.png')
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lagplot.py input_file_path")
        sys.exit(1)
    path = sys.argv[1]
    main(path)
