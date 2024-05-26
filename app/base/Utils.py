import random


BASE58_CHARS = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def get_random_chars(length: int = 4) -> str:
    """Generate a random string of length `length` to be used as a (almost) unique identifier."""
    return "".join(random.choices(BASE58_CHARS, k=length))
