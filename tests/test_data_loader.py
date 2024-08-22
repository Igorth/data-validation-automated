import pytest
from src.data_loader import DataLoader

# Sample data for testing
sample_data = [
    {'id': "1", 'name': "John Doe", "age": "28", "department": "Engineering"},
    {'id': "2", 'name': "Jane Smith", "age": "34", "department": "Marketing"},
]


def test_load_data(mocker):
    # Mock the open function to simulate reading from a file
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data="id,name,age,department\n1,John Doe,28,Engineering\n2,Jane Smith,34,Marketing"))
    data = DataLoader.load_data('../data/sample_data.csv')
    assert data == sample_data


def test_shallow_copy():
    shallow_data = DataLoader.shallow_copy(sample_data)
    assert shallow_data == sample_data
    assert shallow_data is not sample_data  # Ensure it's a new list


def test_deep_copy():
    deep_data = DataLoader.deep_copy(sample_data)
    assert deep_data == sample_data
    assert deep_data is not sample_data  # Ensure it's a new list
    assert deep_data[0] is not sample_data[0]  # Ensure elements are deeply copied


def test_file_not_found(mocker):
    mock_open = mocker.patch("builtins.open", side_effect=FileNotFoundError)
    data = DataLoader.load_data('../data/nonexistent_file.csv')
    assert data == []


def test_empty_file(mocker):
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=""))
    data = DataLoader.load_data('../data/empty_file.csv')
    assert data == []


if __name__ == "__main__":
    pytest.main()
