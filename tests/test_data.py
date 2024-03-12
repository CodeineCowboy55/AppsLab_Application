import pytest
from unittest.mock import patch
from io import StringIO

from application.Data import add_record, my_projectdict, get_record

def test_add_record(monkeypatch, capfd):
    # Mock the input function to provide the necessary inputs for add_record
    mock_inputs = ['10/03/2024', '12/03/2024', 'jmjm55', '123456', '234567', '654321', '4', 'testtype', 'Yes']
    monkeypatch.setattr('builtins.input', lambda prompt: mock_inputs.pop(0))

    # Call the add_record function
    add_record()

    assert my_projectdict[11] == {
        "Request Date": "10/03/2024",
        "Date Required": "12/03/2024",
        "User": "jmjm55",
        "Customer Number": 123456,
        "Project Number": 234567,
        "Fragrance Number": 654321,
        "Dosage": 4.0,
        "Product Type": "testtype",
        "Base": True,
    }

def test_get_record_success(monkeypatch, capfd):
    # Mock the input function to provide the necessary inputs for add_record
    mock_inputs = ['10']
    monkeypatch.setattr('builtins.input', lambda prompt: mock_inputs.pop(0))

    # Call the add_record function
    get_record()

    captured = capfd.readouterr()

    expected_output = "Record found"

    assert expected_output in captured.out


def test_get_record_failure(monkeypatch, capfd):
    # Mock the input function to provide the necessary inputs for add_record
    mock_inputs = ['12']
    monkeypatch.setattr('builtins.input', lambda prompt: mock_inputs.pop(0))

    # Call the add_record function
    get_record()

    captured = capfd.readouterr()

    expected_output = "No record found for ID 12.\n"

    assert captured.out == expected_output
