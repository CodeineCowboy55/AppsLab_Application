import pytest
from unittest.mock import patch
from io import StringIO

##from application.Data import my_projectdict, add_record, get_record, edit_record
from application.Admin import delete_record


def test_incorrect_password(capfd, monkeypatch):

    args_list = ['wrong_password', '2']
    # Mock the input function
    monkeypatch.setattr('builtins.input', lambda _: args_list.pop(0))

    # Call the function with the mocked inputs
    delete_record()

     # Capture the output
    captured = capfd.readouterr()

    # Check if the expected output is printed
    expected_output = "Incorrect password. Deletion denied.\n"
    assert captured.out == expected_output


def test_correct_id_deleted(capfd, monkeypatch):

    args_list = ['Gabagoo13!', '2']
    # Mock the input function
    monkeypatch.setattr('builtins.input', lambda _: args_list.pop(0))

    # Call the function with the mocked inputs
    delete_record()

    # Capture the output
    captured = capfd.readouterr()

    # Check if the expected output is printed
    expected_output = "DELETED 2\n"
    assert captured.out == expected_output


def test_incorrect_id_not_found(capfd, monkeypatch):

    args_list = ['Gabagoo13!', '13']
    # Mock the input function
    monkeypatch.setattr('builtins.input', lambda _: args_list.pop(0))

    # Call the function with the mocked inputs
    delete_record()

    # Capture the output
    captured = capfd.readouterr()

    # Check if the expected output is printed
    expected_output = "ID not found.\n"
    assert captured.out == expected_output


def test_invalid_id_raises_value_error(capfd, monkeypatch):

    args_list = ['Gabagoo13!', 'invalid_id']
    # Mock the input function
    monkeypatch.setattr('builtins.input', lambda _: args_list.pop(0))

    # Call the function with the mocked inputs
    delete_record()

    # Capture the output
    captured = capfd.readouterr()

    # Check if the expected output is printed
    expected_output = "Invalid input. Please enter a valid ID.\n"
    assert captured.out == expected_output
    