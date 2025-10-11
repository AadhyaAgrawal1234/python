import sys

def initial_slambook():
    rows,cols= int(input("Please enter initial number of contacts :")),5
    slam_book = []
    print(slam_book)

    for i in range (rows):
        print("Please enter contact details")
        print("NOTE: *indicates madatory fields*")
        print("....................................................................")
        temp=[]

    for j in range(5):
        if j == 0 :
            temp.append(str(input("Enter Name*: ")))  

            if temp [j] =='' or  temp[j] == ' ' :
                sys.exit (
                    "Name is a mandeetory field, Process exitting due to blank field........"
                )

            if j == 1:
                temp.append (int(input("Enter Phone Number : ")))    
            
            if j == 2:
                temp.append (str(input("Enter e=mail address : ")))

                if temp [j] =='' or  temp[j] == ' ' :
                    temp[j] = None

            if j == 3:
                temp.append (str(input("Enter date of birth [dd/mm/yyyy] : ")))

                if temp [j] =='' or  temp[j] == ' ' :
                    temp[j] = None

            if j == 4:
                temp.append 
                (str(input("Enter category [family/friend/work/others] : ")))

                if temp [j] =='' or  temp[j] == ' ' :
                    temp[j] = None

    slam_book.append(temp)
    print(slam_book)
    return slam_book  
