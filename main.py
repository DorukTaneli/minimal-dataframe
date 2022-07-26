
def print_hello(name):
    print(f'Hello {name}!')


def test_implementation():
    df = ''
    result = df[(df["price"] + 5.0 > 10.0) & (df["sales"] > 3)
                & ~df["taxed"]]["SKU"]
    print(result)


if __name__ == '__main__':
    print_hello('World')
    # test_implementation()

