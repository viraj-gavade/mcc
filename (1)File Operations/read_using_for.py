with open('file1.txt', 'r') as f1:
    for line in f1:
        # print(line)
        print(len(line.strip()))