# JSON-YAML Converter

## Introduction
This Python application is a handy tool for converting data between JSON and YAML, two of the most popular data serialization formats. It offers a straightforward command-line interface for easy use.

## Prerequisites
- Python 3.x
- pyyaml library

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/zLefterov/JSON-to-YAML.git
   ```
2. Navigate to the cloned directory:
   ```sh
   cd JSON-to-YAML
   ```
3. Install the required package:
   ```sh
   pip install pyyaml
   ```

## Usage

Run the script using Python:

```sh
python JSON-to-YAML.git
```

Follow the on-screen prompts to choose the conversion type and specify file paths.

### Example Files

#### `example.json`

```json
{
    "name": "John Doe",
    "age": 30,
    "isStudent": false,
    "hobbies": ["reading", "gaming", "hiking"]
}
```

#### `example.yaml`

```yaml
name: Jane Doe
age: 25
isStudent: true
hobbies:
  - painting
  - photography
  - writing
```

## Testing

The application can be tested with the provided `example.json` and `example.yaml` files.

### JSON to YAML Conversion

1. Choose the JSON to YAML conversion option.
2. Provide the path for `example.json`.
3. Specify the output file path for the YAML file and the new already converted file name with .yml format for example: test-j-to-y.yaml

### YAML to JSON Conversion

1. Select the YAML to JSON conversion option.
2. Enter the path for `example.yaml`.
3.  Specify the output file path for the JSON file and the new already converted file name with .json format for example: test-y-to-j.json

## Contributions

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
