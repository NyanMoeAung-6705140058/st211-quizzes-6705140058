from unittest.mock import Mock

def test_return_value():
    mock = Mock()

    mock.get_status.return_value = "OK"

    assert mock.get_status() == "OK"
