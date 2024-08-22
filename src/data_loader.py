import csv
import copy


class DataLoader:
    @staticmethod
    def load_data(file_path):
        """
        Load data from a CSV file.
        :param file_path: Path to the CSV file
        :return: List of dictionaries representing the rows in the CSV.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except FileNotFoundError:
            print(f"Error: The file at {file_path} does not exist.")
            return []
        except Exception as err:
            print(f"An error occurred while loading the data: {err}")
            return []

    @classmethod
    def shallow_copy(cls, data):
        """
        Create a shallow copy of the data.
        :param data: List of dictionaries (loaded data)
        :return: Shallow copy of the data
        """
        return copy.copy(data)

    @classmethod
    def deep_copy(cls, data):
        """
        Create a deep copy of the data.
        :param data: List of dictionaries (loaded data)
        :return: Deep copy of the data
        """
        return copy.deepcopy(data)
