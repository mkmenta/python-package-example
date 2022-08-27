from helloworld import say_hello


def test_helloworld_no_params():
    assert say_hello() == "\x1b[34mHello world!\x1b[0m"


def test_helloworld_with_param():
    assert say_hello("mkmenta") == "\x1b[32mHello mkmenta!\x1b[0m"
