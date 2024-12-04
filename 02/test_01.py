import p1


def test_single_safe():
    input = [7, 6, 4, 2, 1]
    assert p1.isSafe(input) is True


def test_single_unsafe():
    inputs = [[1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1]]
    for case in inputs:
        assert p1.isSafe(case) is False
