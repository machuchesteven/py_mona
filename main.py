from mona.mapper import Database, Table, Column, ForeignKey

db = Database("./test.db")

class Author(Table):
    name = Column(str)
    lucky_number = Column(int)

class Post(Table):
    title = Column(str)
    published = Column(bool)
    author = ForeignKey(Author)


db.create(Author)
db.create(Post)

author = Author(name="John Doe", lucky_number=7)
db.save(author)

bob = db.get(Author, 47)

all_authors = db.all(Author)

post = Post(title="Hello, World!", published=True, author=author)

db.save(post)

print(db.get(Post, 55).author.name)

if __name__ == '__main__':
    print('This is mona, a cross platform ORM for Python.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
