class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'

        return f'Author: {self.name}\nPublished Books: {book_list}'

    def publish(self, title):

        books_lower = []
        for book in self.books:
            books_lower.append(book.lower())

        if title in self.books:
            print('This book is already in the published list.')
        else:
            self.books.append(title)


author1 = Author('Ryan W')
author1.publish('Title 1')
author1.publish('Title 2')
author1.publish('Title 1')
print(author1)

author2 = Author('Author 2')
print(author2)
