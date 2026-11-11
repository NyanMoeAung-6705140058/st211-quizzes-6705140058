from unittest.mock import patch
import time

def get_timestamp():
    return int(time.time())

def test_mocked_time():
    with patch("time.time", return_value=1000000):
        assert get_timestamp() == 1000000
