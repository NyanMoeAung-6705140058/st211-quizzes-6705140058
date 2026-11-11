import pytest
from unittest.mock import Mock
from payment import OrderProcessor

def test_handles_gateway_failure():
    gateway = Mock()
    gateway.charge.side_effect = ConnectionError("Network down")

    processor = OrderProcessor(gateway)
    with pytest.raises(ConnectionError):
        processor.process(100)
