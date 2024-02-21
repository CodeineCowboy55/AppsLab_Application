import pytest
from io import StringIO
from unittest.mock import patch
from __main__ import main


@pytest.mark.parametrize("user_input, expected_output", [
    ("1\n", "You selected Option 1."),
    ("2\n", "You selected Option 2."),
    ("3\n", "You selected Option 3."),
    ("4\n", "You selected Option 4."),
    ("5\n", "Placeholder for Option 5."),
    ("6\n", "Exiting the program.\n")
])
def test_main(monkeypatch, user_input, expected_output):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('builtins.input', side_effect=[user_input]):
            monkeypatch.setattr('msvcrt.kbhit', lambda: False)
            monkeypatch.setattr('msvcrt.getch', lambda: b'')
            main()
            assert fake_out.getvalue().strip().endswith(expected_output)


def test_invalid_input(monkeypatch):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('builtins.input', side_effect=["invalid\n", "6\n"]):
            monkeypatch.setattr('msvcrt.kbhit', lambda: False)
            monkeypatch.setattr('msvcrt.getch', lambda: b'')
            main()
            assert "Invalid input. Please enter a number." in fake_out.getvalue()


def test_exit_confirmation_yes(monkeypatch):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('builtins.input', side_effect=["6\n"]):
            monkeypatch.setattr('msvcrt.kbhit', lambda: False)
            monkeypatch.setattr('msvcrt.getch', lambda: b'')
            with pytest.raises(SystemExit):
                main()
            assert "Exiting the program." in fake_out.getvalue()


def test_exit_confirmation_no(monkeypatch):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('builtins.input', side_effect=["no\n", "6\n"]):
            monkeypatch.setattr('msvcrt.kbhit', lambda: False)
            monkeypatch.setattr('msvcrt.getch', lambda: b'')
            main()
            assert "Exiting the program." not in fake_out.getvalue()