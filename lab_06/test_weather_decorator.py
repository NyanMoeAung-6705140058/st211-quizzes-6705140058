from unittest.mock import patch
from weather import describe_weather

@patch("weather.get_temperature")
def test_pleasant_weather(mock_temp):
    mock_temp.return_value = 20

    assert describe_weather() == "Pleasant"
