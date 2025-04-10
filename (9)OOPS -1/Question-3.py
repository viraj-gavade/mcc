#3) Write a Python program to illustrate the concept of polymorphism.

#Python prog that illustrates the concept of polymorphism

class Book:

#constructor

    def __init__(self, name, author):

        self.name=name

        self.author=author

#abstract method, defined by convention only

def func1(self):

    raise NotImplementedError ("Subclass must implementabstract method")

#define class as subject and inherit book

class subject (Book):
#redefine method with same name as super class
     def fucn1(self):
         return self.author

class Python (Book):
#redefine method with same name as super class
     def fucn1(self):
         return self.author

#Array of objects
books=[subject('Java','Adam'),Python('simple python','Jim'),subject('Advanced java','Adrew')]
for book in books:
    print("Book Name:",book.name,"and","author of book:",book.fucn1())
