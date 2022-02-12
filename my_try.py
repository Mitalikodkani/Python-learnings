'''
Implement a student library system using OOPS where students can borrow a book from the list of books.
Create a separate library and student class
Your program must be menu driven 
You are free to choose functions and attributes to implement its functionality
'''

class Library:
    def __init__(self,book_list):
        self.book_list = book_list
    
    def displayAllBookNames(self):
        for i in self.book_list:
            print(i)

    def borrow(self,book):
        self.book = book
        self.book_list.remove(book)
        print(f"You have borrowed {self.book}")
        return self.book
    
    def returnBook(self,book):
        self.book = book
        return self.book_list.append(book)

class Student:
    
    def requestBook(self):
        self.book = input("Enter the name of the book you want: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    books = ['engineering ethics', 'digital image processing', 'grokking algorithms', 'java oops']
    # library
    lib = Library(books)
    stud = Student()

    print('''***********Welcome**********************
    Following are the command options:
    1. See All Books
    2. Borrow Book
    3. Return Book
    4. Exit the Library
*****************************************
    ''')
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            lib.displayAllBookNames()
        elif choice == 2:
            lib.borrow(stud.requestBook())
        elif choice == 3:
            lib.returnBook(stud.returnBook())
        elif choice == 4:
            print("Thanks for choosing our library. Have a great day ahead!")
            break
        else:
            print("Enter a valid number")   