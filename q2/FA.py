class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("Issue number must be positive.")


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Science Today", "A. Smith")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time", "Time Staff", 105)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print("Number of pages: " + str(book1.get_number_of_pages()))

print("\nMagazine Information:")
mag1.display_info()
print("Issue number: " + str(mag1.get_issue_number()))

print("\nPublication Information:")
pub2.display_info()

print("\nBook Information:")
book2.display_info()
print("Number of pages: " + str(book2.get_number_of_pages()))

print("\nMagazine Information:")
mag2.display_info()
print("Issue number: " + str(mag2.get_issue_number()))
