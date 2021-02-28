"""The Hello World package."""
from hashlib import blake2b

__name__ = 'helloworld'
__version__ = "0.0.3"
__author__ = 'Mikel Menta Garde'
__url__ = "https://github.com/mkmenta/python-package-example"
__license__ = "MIT License"


def say_hello(name=None):
    """Say hello to the world or someone.

    Args:
        name (str): who you want to greet. If None it will greet the world.

    Returns:
        A string with the greeting.

    """
    if name is None:
        return "Hello world!"

    h = blake2b(digest_size=20)
    h.update(name.encode())
    if h.hexdigest() == 'df543254a1110b5d32d96028cf4b1df9ea96ebbb':
        return "I'm on the radioooooo!!!"

    return f"Hello {name}!"
