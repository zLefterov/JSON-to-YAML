import json
import yaml

def json_to_yaml(json_file, yaml_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    with open(yaml_file, 'w') as file:
        yaml.dump(json_data, file, default_flow_style=False)

def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    with open(json_file, 'w') as file:
        json.dump(yaml_data, file, indent=4)

def main():
    choice = input("Choose conversion type:\n1. JSON to YAML\n2. YAML to JSON\nEnter 1 or 2: ")

    if choice == '1':
        json_file = input("Enter the path of the JSON file: ")
        yaml_file = input("Enter the path for the output YAML file: ")
        json_to_yaml(json_file, yaml_file)
        print(f"Converted {json_file} to {yaml_file}")

    elif choice == '2':
        yaml_file = input("Enter the path of the YAML file: ")
        json_file = input("Enter the path for the output JSON file: ")
        yaml_to_json(yaml_file, json_file)
        print(f"Converted {yaml_file} to {json_file}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
