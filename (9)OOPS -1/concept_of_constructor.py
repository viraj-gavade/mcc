class Book : 
    def __init__(self,title:str,author:str,price:float):
        self.title = title
        self.author = author
        self.price = price
    
    def DisplayBookDetails(self):
        print('Book Details Are as Following:-')
        print('Title of the book:-', self.title)
        print('Author of the book:-', self.author)
        print('Price of the book:-', self.price)


obj = Book('Atomic Habits','James Clear',200)
obj.DisplayBookDetails()