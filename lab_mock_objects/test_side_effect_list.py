from unittest.mock import Mock

def test_side_effect_list():
    mock = Mock()

    mock.get_data.side_effect = [
        "A",
        "B",
        "C"
    ]

    assert mock.get_data() == "A"
    assert mock.get_data() == "B"
    assert mock.get_data() == "C"
