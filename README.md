
# Unit Converter Django Application

This is a simple Django application that allows users to convert between different units of length, weight, and temperature. It provides a user-friendly interface where users can input values, select units, and view the converted result.

## Features
- **Length Conversion**: Converts between units like Millimeters, Centimeters, Inches, Feet, Yards, Miles, Meters, and Kilometers.
- **Temperature Conversion**: Converts between Kelvin, Celsius, and Fahrenheit.
- **Weight Conversion**: Converts between Kilograms, Grams, Milligrams, Pounds, and Ounces.
- **Formatted Output**: Displays the converted values with appropriate unit formatting (e.g., with commas or rounded decimals).

## Installation

### Prerequisites
- Python 3.9 or later
- Django 4.2.17 or later

### Steps to Set Up

1. Clone this repository:
    ```bash
    git clone https://github.com/Kobby24/unit-converter-
  
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Mac/Linux
    .venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database (if applicable):
    ```bash
    python manage.py migrate
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Visit the application in your browser:
    ```
    http://127.0.0.1:8000
    ```

## Project Structure

```
unit-converter/
├── unitconverter/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── length.html
│   │   ├── temp.html
│   │   ├── weight.html
│   │   └── answer.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```

### Template Files
- `index.html`: The main landing page of the application.
- `length.html`: The template for the length unit conversion page.
- `temp.html`: The template for the temperature unit conversion page.
- `weight.html`: The template for the weight unit conversion page.
- `answer.html`: The template to display the results of conversions.

### Views
- `index()`: Renders the index page.
- `answer()`: Renders the results of conversions, displaying both the converted value and the original input value.
- `length()`: Handles the length conversion logic for various units.
- `temp()`: Handles the temperature conversion logic (Kelvin, Celsius, and Fahrenheit).
- `weight()`: Handles the weight conversion logic for kilograms, grams, pounds, ounces, etc.

### Helper Functions
- `format_num()`: A helper function used to format numbers for display, ensuring they include appropriate units and decimal precision.

## How It Works
1. The user selects a unit type (length, temperature, or weight) and the corresponding input/output units.
2. The user inputs a value to convert.
3. The conversion logic processes the input value and performs the necessary calculation using predefined formulas.
4. The result is displayed on a new page with the converted value and the original input.


## Acknowledgments

- This project is built using Django, a powerful Python web framework.
- The unit conversion formulas are sourced from commonly used conversion standards.

  https://roadmap.sh/projects/unit-converter
