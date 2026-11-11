from unittest.mock import Mock

def test_dynamic_side_effect():
    mock = Mock()
    mock.double.side_effect = lambda x: x * 2

    assert mock.double(5) == 10
    assert mock.double(21) == 42
