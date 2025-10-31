import os

with open("Sample_File(2).txt", "w") as f:
    f.write("My name is Aadhya. I am in Class 6. I like Python.")

print("Your introduction is written in Sample_File(2).txt")

with open("Sample_File(2).txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Words in the file are:", words)

if os.path.exists("My_File.txt"):
    print("My_File.txt exists.")
else:
    print("My_File.txt does not exist.")

if not os.path.exists("My_File.txt"):
    with open("My_File.txt", "w") as f:
        f.write("My name is Aadhya. I am in Class 6. I love learning new things!")
    print("My_File.txt is created and your introduction is written.")


if os.path.exists("Sample_File(2).txt"):
    os.remove("Sample_File(2).txt")
    print("Sample_File(2).txt is deleted.")

print("All work is done!")
