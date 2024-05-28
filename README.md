# Project Name

Selenium Python Test

## Requirements

- Python 3

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arthurbrandao0/selenium-python-test.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd selenium-python-test
    ```

3. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

Make sure the virtual environment is activated.

To run the tests, use the following command:

```bash
behave --no-capture -f allure -o logs ./features
```

This command will execute the tests and generate data for the report (Allure Report).

## Displaying the Report

After generating the data with the command above, the report can be displayed using the following command:

```bash
allure serve logs
```