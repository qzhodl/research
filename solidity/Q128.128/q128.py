#!/usr/bin/env python3
import sys

def float_to_q128_128(f):
    return int(f * 2**128)

def q128_128_to_float(q):
    return q / 2**128

def main():
    # get the input type, either float or q128.128
    input_type = sys.argv[1]
    # get the input value
    input_value = sys.argv[2]

    if input_type == "float":
        print(float_to_q128_128(float(input_value)))
    elif input_type == "q128.128":
        print(q128_128_to_float(int(input_value)))

if __name__ == "__main__":
    main()

