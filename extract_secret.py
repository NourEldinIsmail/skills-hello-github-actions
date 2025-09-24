import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        # add $ after the first character
        manipulated_string = input_string[0] + '$' + input_string[1:]
        print(f"Received string: {input_string}")
        print(f"Manipulated string: {manipulated_string}")
    else:
        print("No string argument provided")