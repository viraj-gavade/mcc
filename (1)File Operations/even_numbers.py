def even(a):
    if a % 2 == 0:
        print(a)

with open('even_numbers.txt', 'r') as f1:
    for line in f1:
        even(int(line.strip()))