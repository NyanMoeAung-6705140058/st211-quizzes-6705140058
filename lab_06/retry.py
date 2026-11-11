def charge_with_retry(gateway, amount, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return gateway.charge(amount)
        except ConnectionError:
            if attempt == max_attempts - 1:
                raise
    return None
