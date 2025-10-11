file = open ( 'Sample_File.txt','r')
print(file.read())
file.close()

file = open ( 'Sample_File.txt','r')
print("\n Read in Parts\n")
print(file.read(10))
file.close()

file = open ( 'Sample_File.txt','r')
print("Read first line........")
print(file.readline())
file.close()


file = open ( 'Sample_File.txt','r')
print("Read 4 lines........")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open ( 'Sample_File.txt','r')
print("Looping through the lines......")
for line in file : 
 print(line)
file.close()