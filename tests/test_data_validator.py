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


if __name__ == '__main__':
    pytest.main()
