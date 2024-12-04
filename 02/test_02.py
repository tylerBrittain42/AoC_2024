import p2


def test_single_safe_no_removal():
    input = [7, 6, 4, 2, 1]
    assert p2.bigIsSafe(input) is True


def test_single_safe_removal():
    inputs = [[1, 3, 2, 4, 5], [8, 6, 4, 4, 1]]
    for case in inputs:
        assert p2.bigIsSafe(case) is True


def test_single_unsafe():
    inputs = [[1, 2, 7, 8, 9], [9, 7, 6, 2, 1]]
    for case in inputs:
        assert p2.bigIsSafe(case) is False


def test_failing_case():
    input = [89, 84, 82, 81, 80]
    assert p2.bigIsSafe(input) is True
