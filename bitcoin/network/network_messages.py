# network/network_messages.py

import json


def create_message(type, data):
    """
    Creates a JSON-formatted message for network communication.
    """
    return json.dumps({"type": type, "data": data})


def parse_message(message):
    """
    Parses a JSON-formatted network message.
    """
    return json.loads(message)
