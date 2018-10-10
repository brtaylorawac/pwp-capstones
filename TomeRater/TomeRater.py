class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        if address.find("@") != -1 and (address.lower().find(".com") != -1 or address.lower().find(".edu") != -1 or address.lower().find(".org") != -1):
            self.email = address
            print("User email has been updated to " + self.email)
        else:
            print(address + " is not a valid email.")

    def __repr__(self):
        return ("User: " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books)))

    def __eq__(self, other_user):
        return (self.name == other_user.name and self.email == other_user.email)

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        num_books_rated = 0
        for book in self.books.values():
            if book != None:
                num_books_rated += 1
                total_rating += book
        if num_books_rated > 0:
            return total_rating/num_books_rated
        else:
            return 0


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("Book isbn has been updated to " + str(self.isbn))
        
    def add_rating(self, rating):
        if rating == None:
            print("Invalid Rating")
        elif rating >= 0 and rating <= 4:
            self.rating.append(rating)
        else:
            print("Invalid Rating")
            
    def get_average_rating(self):
        if len(self.rating) == 0:
            return 0
        else:
            total = 0
            for rate in self.rating:
                total += rate
            return total/len(self.rating)
      

    def __eq__(self, other_book):
        return (self.title == other_book.title and self.isbn == other_book.isbn)

    def __hash__(self):
        return hash((self.title, self.isbn))
      
    def __repr__(self):
        return (self.title)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return (self.title + " by " + self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return (self.title + " a " + self.level + " manual on " + self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        for book in self.books:
            if book.get_isbn == isbn:
                print("ISBN for " + title + " is not unique.")
                return None
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                print("ISBN for " + title + " is not unique.")
                return None
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        for book in self.books:
            if book.get_isbn == isbn:
                print("ISBN for " + title + " is not unique.")
                return None
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email)
        if email in self.users:
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + email + "!")

    def add_user(self, name, email, user_books = None):
        if email.find("@") != -1 and (email.lower().find(".com") != -1 or email.lower().find(".edu") != -1 or email.lower().find(".org") != -1):            
            if email in self.users:
                print("Email " + email + " already exists")
            else:
                user = User(name, email)
                self.users[email] = user
                if user_books != None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
        else:
            print(email + " is not a valid email.")

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def get_most_read_book(self):
        book = None
        most_read = 0
        for book_key, book_value in self.books.items():
            if book_value > most_read:
                book = book_key
                most_read = book_value

        return book

    def highest_rated_book(self):
        book = None
        highest_rated = 0
        for book_key in self.books:
            if book_key.get_average_rating() > highest_rated:
                book = book_key
                highest_rated = book_key.get_average_rating()

        return book

    def most_positive_user(self):
        user = None
        highest_rated = 0
        for user_value in self.users.values():
            if user_value.get_average_rating() > highest_rated:
                user = user_value
                highest_rated = user_value.get_average_rating()

        return user