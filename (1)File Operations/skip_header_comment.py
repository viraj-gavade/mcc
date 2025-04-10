def skip_header(file1):
    data = file1.readline().strip()
    return data

def skip_comment(file2):
    for i in file2:
        if i.startswith('#'):
            continue
        else:
            print(i.strip())

with open('file1.txt', 'r') as file3:
    skip_header(file3)
    skip_comment(file3)
