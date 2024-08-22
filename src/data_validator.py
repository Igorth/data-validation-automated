class DataValidator:
    @staticmethod
    def validate_columns(data, required_columns):
        """
        Validate that all required columns are present in the data
        :param data: List of dictionaries representing the data.
        :param required_columns: List of required column names.
        :return: Boolean indicating whether all required columns are present.
        """
        if not data:
            return False
        data_columns = set(data[0].keys())
        return all(col in data_columns for col in required_columns)

    @staticmethod
    def validate_data_types(data, column_types):
        """
        Validate that each column in the data matches the expected type.
        :param data: List of dictionaries representing the data.
        :param column_types: Dictionary with column names as keys and expected types as values.
        :return: Boolean indicating whether all data types are valid.
        """
        for row in data:
            for col, expected_type in column_types.items():
                if col in row and not isinstance(row[col], expected_type):
                    try:
                        row[col] = expected_type(row[col])
                    except ValueError:
                        return False
        return True

    @staticmethod
    def check_missing_values(data):
        """
        Check for missing values in the data.
        :param data: List of dictionaries representing the data
        :return: Boolean indicating whether any missing values are found
        """
        for row in data:
            if any(value == '' or value is None for value in row.values()):
                return False
        return True
