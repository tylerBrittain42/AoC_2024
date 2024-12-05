import p2


def test_getOps():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

    assert p2.getOps(input) == expected


def test_calcOp():
    inputs = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    expected = [8, 25, 88, 40]

    for i in range(0, len(inputs)):
        assert p2.calcOp(inputs[i]) == expected[i]


def test_filter():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected = "xmul(2,4)&mul[3,7]!^?mul(8,5))"

    assert p2.init_filter(input) == expected


def test_calcFilter():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert p2.calcFiltered(input) == 48
