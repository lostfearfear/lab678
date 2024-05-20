
import json
import sys
import os

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe path_to_input_file path_to_output_file")
        sys.exit(1)

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]

    valid_extensions = ['.xml', '.json', '.yml', '.yaml']
    input_extension = os.path.splitext(input_filepath)[1]
    output_extension = os.path.splitext(output_filepath)[1]

    if input_extension not in valid_extensions or output_extension not in