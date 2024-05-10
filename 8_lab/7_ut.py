from lab_7 import tt1, tt2, tt3, tt4


def test_b1():
    assert tt1.b1(5) == 8


def test_b2():
    a, b = tt2.b2("кокошнель")
    print(a)
    assert a == 2 and b == 'ко'


def test_b3():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    assert tt3.b3(matrix) == 15


def test_b4():
    assert tt4.b4("привет это я", "привет") == 6
