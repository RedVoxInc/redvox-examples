"""
Provide top level module documentation briefly describing this example.
A longer description can be provided in the README.

Don't worry about dates/authors/etc this is all tracked by git.
"""


def say_hello(name: str) -> str:
    """
    Document your functions. Document inputs and outputs.
    :param name: The name to say hello to.
    :return: A string that greets the passed in name.
    """
    return f"hello, {name}"


def main() -> None:
    # Document complicated pieces of code
    print(say_hello("HAL"))


if __name__ == "__main__":
    main()
