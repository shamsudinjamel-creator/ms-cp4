import sys

def main():
    # Read all lines from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse the inputs as specified
    diameter = float(input_data[0])
    width_per_knight = float(input_data[1])
    num_knights = int(input_data[2])

    # Define the exact value of PI required by the problem
    PI = 3.1415926535

    # Calculate available circumference and total required space
    circumference = diameter * PI
    required_space = width_per_knight * num_knights

    # Compare and output the result
    if circumference >= required_space:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
