from unittest.mock import patch
from payment import PaymentGateway, OrderProcessor

def test_patch_gateway_method():
    with patch.object(PaymentGateway, "charge", return_value="MOCKED"):
        gateway = PaymentGateway()
        processor = OrderProcessor(gateway)
        result = processor.process(50)

        assert "MOCKED" in result
