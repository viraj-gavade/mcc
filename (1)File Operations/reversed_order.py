with open('file1.txt', 'r') as f1:
    c = f1.readlines()
    for p in reversed(c):
        # print(line)
        print((p.strip()))