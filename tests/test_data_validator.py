import pytest
from src.data_loader import DataLoader
from src.data_validator import DataValidator

# Load data from the CSV file
data = DataLoader().load_data('../data/sample_data.csv')


def test_validate_columns():
    # Validate required columns
    required_columns = ['id', 'name', 'age', 'department']
    columns_valid = DataValidator.validate_columns(data, required_columns)
    print(f"Columns valid: {columns_valid}")


def test_validate_data_types():
    column_types = {'id': int, 'name': str, 'age': int, 'department': str}
    types_valid = DataValidator.validate_data_types(data, column_types)
    print(f"Data types valid: {types_valid}")


def test_check_missing_values():
    missing_values = DataValidator.check_missing_values(data)
    print(f"Missing values: {missing_values}")


if __name__ == '__main__':
    pytest.main()
