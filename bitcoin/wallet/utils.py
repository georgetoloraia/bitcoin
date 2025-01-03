# wallet/utils.py


def validate_address(address):
    """
    Validates the format of a cryptocurrency address.
    """
    # Add logic for address format validation
    return len(address) == 34 and address.startswith("1")
