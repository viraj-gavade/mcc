import os

print("Current directory:", os.getcwd())

os.mkdir("test_dir")

os.chdir("test_dir")
print("After chdir:", os.getcwd())

os.chdir("..")
os.rmdir("test_dir")
print("Directory removed.")
