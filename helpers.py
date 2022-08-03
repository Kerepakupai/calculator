from socket import inet_ntoa


def add(n1: float, n2: float) -> float:
    """"""
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    return round(n1 / n2, ndigits=2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
