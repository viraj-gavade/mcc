with open("file1.txt", "w") as f:
    f.write("This is line one.\n")
    f.write("This is line two.\n")

with open("file1.txt", "a") as f:
    f.write("This is an appended line.\n")
    f.write("Another appended line.\n")

with open("file1.txt", "r") as f:
    print(f.read())
