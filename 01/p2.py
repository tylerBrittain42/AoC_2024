FILE_NAME = 'input_1.txt'
# FILE_NAME = 'sample.txt'

def main():
    first = []
    second = []
    sim_score = 0

    # Get two lists
    with open(FILE_NAME, 'r') as f:
        for line in f:
            pair = line.split('   ')
            first.append(int(pair[0]))
            second.append(int(pair[1].strip()))

    frequency_chart = get_frequency(second)

    for ele in first:
        sim_score += get_score(ele, frequency_chart)

    print(sim_score)

def get_score(val:int, chart:dict) -> int:
        cur_freq = chart.get(val)
        return 0 if cur_freq is None else cur_freq * val


def get_frequency(to_be_scored:list) -> dict:
    scoreCard = {}
    for ele in to_be_scored:
        if scoreCard.get(ele) is not None:
            scoreCard[ele] += 1
        else:
            scoreCard[ele] = 1
    return scoreCard


if __name__ == '__main__':
    main()
