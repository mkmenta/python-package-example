"""Say hello function usage example."""
from helloworld import say_hello

if __name__ == '__main__':
    # Generate "Hello world!"
    greeting = say_hello()
    print(greeting)

    # Generate "Hello mkmenta!"
    greeting = say_hello("mkmenta")
    print(greeting)
