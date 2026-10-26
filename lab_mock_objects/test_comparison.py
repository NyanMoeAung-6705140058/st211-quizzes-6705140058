from unittest.mock import Mock

def test_comparison():
    mock = Mock()

    mock.fetch.return_value = "STATIC"

    assert mock.fetch() == "STATIC"
    assert mock.fetch() == "STATIC"
    assert mock.fetch() == "STATIC"
