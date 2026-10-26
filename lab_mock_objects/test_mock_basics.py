from unittest.mock import Mock

def test_mock_basics():
    mock = Mock()

    result = mock.some_method()

    print(result)

    assert isinstance(result, Mock)
