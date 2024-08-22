from src.data_processing_workflow import process_data
from src.report_generator import ReportGenerator

if __name__ == '__main__':
    # Define the file path and validation criteria
    file_path = '../data/sample_data.csv'
    required_columns = ['id', 'name', 'age', 'department']
    column_types = {'id': int, 'name': str, 'age': int, 'department': str}

    # Process the data
    valid_data = process_data(file_path, required_columns, column_types)

    if valid_data:
        # Generate a summary report
        report = ReportGenerator.generate_summary_report(valid_data)
        print(report)

        # Save the summary report to a file
        ReportGenerator.save_report(report, '../reports/summary_report.txt')
        print("Summary report saved as 'reports/summary_report.txt.")

        # Generate and save a CSV report
        ReportGenerator.generate_csv_report(valid_data, '../reports/data_report.csv')
        print("CSV report saved as 'reports/data_report.csv'.")


