import csv
from datetime import datetime


class ReportGenerator:
    @staticmethod
    def generate_summary_report(data):
        """
        Generate a summary report from the data
        :param data: List of dictionaries representing the data.
        :return: String containing the summary report
        """
        if not data:
            return "No data available to generate summary report"

        total_records = len(data)
        columns = list(data[0].keys())
        column_summary = {col: set() for col in columns}

        for row in data:
            for col in columns:
                column_summary[col].add(row[col])

        report = f"\nData Summary Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"Total Records: {total_records}\n\n"
        for col, values in column_summary.items():
            report += f"Column '{col}': {len(values)} unique values\n"
            if len(values) <= 5:
                report += f"Values: {', '.join(map(str, values))}\n"
            report += "\n"

        return report

    @staticmethod
    def save_report(report, file_path):
        """
        Save the generated report to a text file
        :param report: String containing the report
        :param file_path: File path where the report will be saved
        """
        with open(file_path, 'w') as file:
            file.write(report)

    @staticmethod
    def generate_csv_report(data, file_path):
        """
        Generate and save a CSV report from the data.
        :param data: List of dictionaries representing the data
        :param file_path: File path where the CSV report will be saved
        """
        if not data:
            raise ValueError("No data available to generate the report.")

        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
