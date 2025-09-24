import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        print(f"Received string: {input_string}")
    else:
        print("No string argument provided")