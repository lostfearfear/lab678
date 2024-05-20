import json
import yaml
import sys
import os

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe path_to_input_file path_to_output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = ['.xml', '.json', '.yml', '.yaml']
    input_ext = os.path.splitext(input_file)[1]
    output_ext = os.path.splitext(output_file)[1]

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print("Supported formats are: .xml, .json, .yml, .yaml")
        sys.exit(1)

    return input_file, output_file

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, indent=4)

if name == "main":
    input_file, output_file = parse_args()
    input_ext = os.path.splitext(input_file)[1]
    output_ext = os.path.splitext(output_file)[1]

    if input_ext == '.json':
        data = read_json(input_file)
    elif input_ext in ['.yml', '.yaml']:
        data = read_yaml(input_file)
    else:
        print(f"Unsupported input file format: {input_ext}")
        sys.exit(1)

    if output_ext == '.json':
        write_json(data, output_file)
    elif output_ext in ['.yml', '.yaml']:
        write_yaml(data, output_file)
    else:
        print(f"Unsupported output file format: {output_ext}")
        sys.exit(1)