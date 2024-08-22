import pytest
from src.data_validator import DataValidator

# Sample data for testing purposes
valid_data = [
    {"id": "1", "name": "John Doe", "age": "28", "department": "Engineering"},
    {"id": "2", "name": "Jane Smith", "age": "34", "department": "Marketing"},
]

missing_column_data = [
    {"id": "1", "name": "John Doe", "age": "28"},
    {"id": "2", "name": "Jane Smith", "age": "34"},
]

invalid_type_data = [
    {"id": "1", "name": "John Doe", "age": "twenty-eight", "department": "Engineering"},
    {"id": "2", "name": "Jane Smith", "age": "thirty-four", "department": "Marketing"},
]

missing_value_data = [
    {"id": "1", "name": "John Doe", "age": "", "department": "Engineering"},
    {"id": "2", "name": "Jane Smith", "age": "34", "department": None},
]


def test_validate_columns():
    required_columns = ['id', 'name', 'age', 'department']
    assert DataValidator.validate_columns(valid_data, required_columns) is True
    assert DataValidator.validate_columns(missing_column_data, required_columns) is False


def test_validate_data_types():
    column_types = {'id': int, 'name': str, 'age': int, 'department': str}
    assert DataValidator.validate_data_types(valid_data, column_types) is True
    assert DataValidator.validate_data_types(invalid_type_data, column_types) is False


def test_check_missing_values():
    assert DataValidator.check_missing_values(valid_data) is True
    assert DataValidator.check_missing_values(missing_value_data) is False


if __name__ == '__main__':
    pytest.main()
