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
