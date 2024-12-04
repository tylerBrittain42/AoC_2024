FILE_NAME = "sample.txt"
FILE_NAME = "input.txt"


def main():
    safe_count = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            levels = [int(item) for item in line.split(" ")]
            levels = [int(item) for item in line.split(" ")]
            if bigIsSafe(levels):
                safe_count += 1

    print(f"safe count: {safe_count}")


def bigIsSafe(levels: list) -> bool:
    res = isSafe(levels)
    if res == -1:
        return True
    else:
        for i in range(0, len(levels)):
            levelsCopy = levels[:]
            levelsCopy.pop(i)
            if isSafe(levelsCopy) == -1:
                return True

    return False


# Two conditions to be safe:
# 1. levels are either all decreasing or all increasing
# 2. Difference between adj levels is at least one and less than 4
def isSafe(levels: list, skipped=False) -> int:
    incDesc = None
    min = 1
    max = 3

    # determining inc or dec
    if levels[0] > levels[1]:
        incDesc = "desc"
    elif levels[0] < levels[1]:
        incDesc = "inc"
    else:
        # print(f"first two are equal {levels[0]} {levels[1]}")
        return 0

    for i in range(0, len(levels) - 1):
        if (incDesc == "desc" and levels[i] < levels[i + 1]) or (
            incDesc == "inc" and levels[i] > levels[i + 1]
        ):
            # print("swapped asc/desc")
            return i
        diff = abs(levels[i] - levels[i + 1])
        if not min <= diff <= max:
            # print(f"diff is {diff}")
            return i

    return -1


if __name__ == "__main__":
    main()