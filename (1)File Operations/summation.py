with open('even_numbers.txt', 'r') as f1:
    sum = 0
    for i in f1:
       a =  int(i.strip())
       sum += a
print("Summation is :-",sum)