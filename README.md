# Automated Data Validation Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-yellow.svg)

## Overview

This project is an Automated Data Validation Tool that processes and validates data from CSV files. It generates summary and CSV reports based on the validation results. The tool consists of several modules and integrates with a CI/CD pipeline to automate testing and report generation.

## Project Structure

- **`.github/workflows/ci.yml`**: GitHub Actions configuration for continuous integration and deployment.
- **`data/sample_data.csv`**: Sample data file used for validation.
- **`reports/`**: Directory where generated reports are saved.
- **`src/`**:
  - **`data_loader.py`**: Contains `DataLoader` class for loading data from CSV files.
  - **`data_processing_workflow.py`**: Main script that processes the data and integrates validation and report generation.
  - **`data_validator.py`**: Contains `DataValidator` class for validating data columns and types.
  - **`report_generator.py`**: Contains `ReportGenerator` class for generating and saving summary and CSV reports.
- **`tests/`**:
  - **`test_data_loader.py`**: Tests for the `DataLoader` class.
  - **`test_data_validator.py`**: Tests for the `DataValidator` class.
  - **`test_report_generator.py`**: Tests for the `ReportGenerator` class.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Igorth/data-validation-automated
   cd data-validation-automated
    ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
    ```
## Usage
1. **Prepare Data:**

Place your CSV data file in the data/ directory. The sample file sample_data.csv is provided as an example.

2. **Run the Data Processing Workflow:**

Execute the main data processing script to load, validate, and generate reports:
```commandline
python src/data_processing_workflow.py
```
This script will:

- Load the data from the specified CSV file.
- Validate the data columns and types.
- Generate a summary report and a CSV report in the reports/ directory.

3. **Check Generated Reports:**

After running the script, you can find the generated reports in the `reports/` directory. The reports include:

- `summary_report.txt`: A summary of the data validation results.
- `data_report.csv`: The CSV version of the validated data

## Testing
To run the tests for the individual modules, use `pytest`:
```commandline
pytest tests/test_data_loader.py
pytest tests/test_data_validator.py
pytest tests/test_report_generator.py
```
## CI/CD Integration
The GitHub Actions configuration file `.github/workflows/ci.yml` sets up a continuous integration pipeline that:

- Runs tests for each push or pull request to the `main` branch.
- Generates reports using the `data_processing_workflow.py` script.
- Uploads generated reports as artifacts.

## Results
- **Validation:** The tool checks for required columns, validates data types, and ensures no missing values.
- **Reports:** Generated reports provide insights into the data validation process, including the total number of records and unique values per column.
