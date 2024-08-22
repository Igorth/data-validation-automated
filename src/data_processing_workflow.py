from src.data_loader import DataLoader
from src.data_validator import DataValidator


def process_data(file_path, required_columns, column_types):
    try:
        # Load data
        print("Loading data...")
        data = DataLoader.load_data(file_path)
        if not data:
            raise ValueError("No data found. The file might be empty or invalid.")
        print("Data loaded successfully.")

        # Validate columns
        print("Validating required columns...")
        if not DataValidator.validate_columns(data, required_columns):
            raise ValueError(f"Missing required columns: {required_columns}")
        print("Required columns validated successfully.")

        # Validate data types
        print("Validating data types...")
        if not DataValidator.validate_data_types(data, column_types):
            raise ValueError("Data type validation failed.")
        print("Data types validated successfully.")

        # Check for missing values
        print("Checking for missing values...")
        if not DataValidator.check_missing_values(data):
            raise ValueError("Missing values found in the data.")
        print("No missing values found.")

        # Proceed with valid data
        print("Data is valid. Proceeding with further processing...")

        return data

    except ValueError as e:
        print(f"Data validation error: {e}")
        return None


if __name__ == "__main__":
    # Define the file path and validation criteria
    file_path = "../data/sample_data.csv"
    required_columns = ['id', 'name', 'age', 'department']
    column_types = {'id': int, 'name': str, 'age': int, 'department': str}

    # Run the data processing workflow
    valid_data = process_data(file_path, required_columns, column_types)
    if valid_data:
        print("Data processing completed successfully.")
    else:
        print("Data processing failed due to validation errors.")
