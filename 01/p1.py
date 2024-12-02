FILE_NAME = 'input_1.txt'

def main():
    first = []
    second = []
    differences = 0

    # Get two lists
    with open(FILE_NAME, 'r') as f:
        for line in f:
            pair = line.split('   ')
            first.append(int(pair[0]))
            second.append(int(pair[1].strip()))

    first.sort()
    second.sort()

    for i in range(0, len(first)):
        differences += abs(first[i] - second[i])


    print(differences)






if __name__ == '__main__':
    main()
