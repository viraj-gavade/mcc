with open('even_numbers.txt', 'r') as f1:
    list1=[]
    for i in f1:
        a = i.split()
        for p in a:
            if p.startswith('1') or p.startswith('2') or p.startswith('3') or p.startswith('4') or p.startswith('5') or p.startswith('6') or p.startswith('7') or p.startswith('8') or p.startswith('9'):
                list1.append(int(p))
            else:
                continue

even_list = []
odd_list = []

for i in list1:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

with open('odd.txt', 'w') as f2:
    str1 = str(odd_list)
    f2.write(str1)

with open('even.txt', 'w') as f3:
    str2 = str(even_list)
    f3.write(str2)
    