"""Miscellaneous functions."""


def do_nothing():
    """A function that does basically nothing."""
    if False:
        print("HEY! I'm doing something!")


class A:
    def __len__(self):
        pass


class B(A):
    """B class."""

    def __len__(self):
        """Get length."""
        return 1
