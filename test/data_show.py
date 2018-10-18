from pandas import read_csv


rating_path = "../dataset/ratings.csv"
book_path = "../dataset/books.csv"
user_path = "../dataset/users.csv"

ratings = read_csv(rating_path)
books = read_csv(book_path)
users = read_csv(user_path)

print(ratings.columns)
print(books.columns)
print(users.columns)

