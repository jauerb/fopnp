"""Utility functions for Google API"""


def load_key(filename="google.key"):
    """Load API key from the specified filename."""
    with open("google.key") as f:
        return f.read().strip()
