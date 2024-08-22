import pytest
from src.report_generator import ReportGenerator

# Sample data for testing
valid_data = [
    {"id": "1", "name": "John Doe", "age": "28", "department": "Engineering"},
    {"id": "2", "name": "Jane Smith", "age": "34", "department": "Marketing"},
]

empty_data = []


def test_generate_summary_report():
    report = ReportGenerator.generate_summary_report(valid_data)
    assert "Total Records: 2" in report
    assert "Column 'id': 2 unique values" in report


def test_generate_summary_report_empty():
    report = ReportGenerator.generate_summary_report(empty_data)
    assert report == "No data available to generate summary report"


def test_generate_csv_report(tmp_path):
    csv_file = tmp_path / 'test_report.csv'
    print(csv_file)
    ReportGenerator.generate_csv_report(valid_data, csv_file)

    with open(csv_file, 'r') as file:
        content = file.read()
        assert "id,name,age,department" in content
        assert "1,John Doe,28,Engineering" in content
        assert "2,Jane Smith,34,Marketing" in content


if __name__ == "__main__":
    pytest.main()
