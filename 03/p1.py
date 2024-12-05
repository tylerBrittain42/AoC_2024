import re


INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def main():
    sum = 0
    with open(INPUT_FILE, "r") as f:
        for line in f:
            ops = getOps(line)
            for op in ops:
                sum += calcOp(op)

    print(sum)


def getOps(stream: str) -> list:
    pattern = r"mul\(\d+,\d+\)"
    res = re.findall(pattern, stream)
    return res


def calcOp(op: str) -> int:
    pattern = r"\w+\((\d+),(\d+)\)"
    res = re.findall(pattern, op)
    a, b = [int(item) for item in res[0]]
    return a * b


if __name__ == "__main__":
    main()
