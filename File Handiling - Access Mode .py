file_read= open('Nature.txt','r')
print("Print file in read mode - ")
print(file_read.read())
file_read.close

file_write = open('Nature.txt','w')
file_write.write("File in write mode......")
file_write.write("Hi! I am Pengu the Penguin . I am 1 year old")
file_write.close()

file_append = open('Nature.txt','a')
file_append.write("\n File in append mode......")
file_append.write("Hi! I am a boy and I have a sister named Pegi. ")
file_append.close()