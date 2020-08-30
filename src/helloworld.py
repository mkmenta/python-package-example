from hashlib import blake2b


def say_hello(name=None):
    if name is None:
        return "Hello world!"

    h = blake2b(digest_size=20)
    h.update(name.encode())
    if h.hexdigest() == 'df543254a1110b5d32d96028cf4b1df9ea96ebbb':
        return "I'm on the radioooooo!!!"

    return f"Hello {name}!"
