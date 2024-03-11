import pytest
from io import StringIO
from unittest.mock import patch

from Assignment.Data import add_record, my_projectdict
from main import main


def test_dummy():
    assert True

def test_addrecord_sucess():
    add_record()
#enter request date in to standar input, then date required in to standard input, enter user name, customer number
#once data is entered we have to check that it what we expect
    assert my_projectdict["dummy"]==
