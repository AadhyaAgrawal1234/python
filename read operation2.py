file = open ( 'Codingal.txt','r')
print("Read first line........")
print(file.readline())
file.close()


file = open ( 'Codingal.txt','r')
print("Read 3 lines........")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open ( 'Codingal.txt','r')
print("Looping through the lines......")
for line in file : 
 print(line)
file.close()