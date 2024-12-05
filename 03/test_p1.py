import p1


def test_getOps():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

    assert p1.getOps(input) == expected


def test_calcOp():
    inputs = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    expected = [8, 25, 88, 40]

    for i in range(0, len(inputs)):
        assert p1.calcOp(inputs[i]) == expected[i]
