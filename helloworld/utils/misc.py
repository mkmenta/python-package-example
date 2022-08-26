"""Miscellaneous functions."""


def do_nothing():
    """Do basically nothing."""
    if False:
        print("HEY! I'm doing something!")


class A:
    """A class."""

    def __len__(self):
        """Get length."""
        pass


class B(A):
    """B class."""

    def __len__(self):
        """Get length."""
        return 1
