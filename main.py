"""
Kitob (Book) klassi malumotlari
Auto-generated Solution
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Kitob nomi: {self.title}")
        print(f"Muallif: {self.author}")
        print(f"Narxi: {self.price} so'm")

if __name__ == "__main__":
    kitob1 = Book("O'tgan kunlar", "Abdulla Qodiriy", 35000)
    kitob1.display_info()
