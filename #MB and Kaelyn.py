#MB and Kaelyn
#1/10/24
#Books-to-read list


#functions
 
list= []

print("Welcome to your books-to-read list. Right now, your list is empty. Choose option 1 to add books.")

def add(): 
    book= input("Choose a book to add to your list: ")
    list.append(book)


def display(): 
    print(list)


def read():
    ans = input("Which book would you like to mark as read?")
    i = list.index(ans)
    list[i]= ans + "X"
    print(list)

def remove():
    ans = int(input("Which number on your list would you like to remove?"))
    list.pop(ans - 1)

def removeall():
    list.clear()

def sort():
    
    list.sort()
    

def count():
    list.count(3)

#main
while True:  
    print("Manual:\n 1.Add book to list \n 2.Display list \n 3.Mark book as read \n 4.Remove book from list \n 5.Count the number of items on your list \n 6.Remove all books from list \n 7.Sort your list alphabetically \n 8.Quit program" )
    option=int(input("option:"))   
    if (option==1): 
        add()
    if (option==2):
        display()

    if (option==3):
        read()

    if (option==4):
        remove()

    if (option==5):
        count()
    if (option==6):
        removea1
        all()
    if (option==7):
        sort()
    if (option==8):
        quit()
    