from unittest.mock import Mock
from payment import OrderProcessor

def test_processor_charges_correct_amount():
    gateway = Mock()
    gateway.charge.return_value = "OK"

    processor = OrderProcessor(gateway)
    processor.process(250)

    gateway.charge.assert_called_once_with(250)

def test_processor_does_not_charge_on_invalid():
    gateway = Mock()
    processor = OrderProcessor(gateway)

    try:
        processor.process(-10)
    except ValueError:
        pass

    gateway.charge.assert_not_called()
