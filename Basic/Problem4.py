import os

path = "python" 

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)