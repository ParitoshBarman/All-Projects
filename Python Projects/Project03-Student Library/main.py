class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    
    def displayAvailableBooks(self):
        print("Books present in library are --> ")
        i = 1
        for book in self.books:
            print(f"\t{i}* {book}")
            i += 1
            
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.  Please keep it safe and return it 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry this book is either not available or has already been issued to someone else. Please wait until the book is available ")
            return False
        
    

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!  Hope you enjoyed reading it!  Have great day ahead!")



class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow--> ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return--> ")
        return self.book



if __name__ == "__main__":
    centralLibrary = Library(["Algarithams", "Django", "Clrs", "Python Notes"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n\n\n======= Welcome to Central Library =======
        Please an option: 
        1. List  all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''

        print(welcomeMsg)
        a = int(input("Enter a choice--> "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library.  Have great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
