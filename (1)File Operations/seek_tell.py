with open("sample.txt", "w") as f:
    f.write("Hello World!")

with open("sample.txt", "r") as f:
    print("Initial position:", f.tell())
    f.seek(6)
    print("Position after seek(6):", f.tell())
