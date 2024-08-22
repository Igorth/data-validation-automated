from src.data_loader import DataLoader

# Load data from the CSV file
data = DataLoader.load_data('../data/sample_data.csv')

# Create a shallow copy of the data
shallow_data = DataLoader.shallow_copy(data)

# Create a deep copy of the data
deep_data = DataLoader.deep_copy(data)

# Check results
print(f'Original data: {data}')
print(f'\nShallow copy: {shallow_data}')
print(f'\nDeep copy: {deep_data}')
