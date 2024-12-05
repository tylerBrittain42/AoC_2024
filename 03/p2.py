import re


INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"
deleteMode = False


def main():
    sum = 0
    with open(INPUT_FILE, "r") as f:
        for line in f:
            sum += calcFiltered(line)

    print(sum)


def calcFiltered(stream: str) -> int:
    line_sum = 0

    filtered = init_filter(stream)
    ops = getOps(filtered)
    for op in ops:
        line_sum += calcOp(op)
    return line_sum


def getOps(stream: str) -> list:
    pattern = r"mul\(\d+,\d+\)"
    res = re.findall(pattern, stream)
    return res


def calcOp(op: str) -> int:
    pattern = r"\w+\((\d+),(\d+)\)"
    res = re.findall(pattern, op)
    a, b = [int(item) for item in res[0]]
    return a * b


def init_filter(stream: str) -> str:
    # Doing this bc the flag should only be set once in the beginning not once each line and I have a headache
    global deleteMode
    result = re.split(r"(don\'t\(\)|do\(\))", stream)

    parsed = []
    print(result)

    while len(result) != 0:
        if result[0] == "don't()":
            deleteMode = True
            result.pop(0)
        elif result[0] == "do()":
            deleteMode = False
            result.pop(0)
        elif deleteMode:
            result.pop(0)
        elif not deleteMode:
            parsed.append(result.pop(0))

    return "".join(parsed)


if __name__ == "__main__":
    main()
