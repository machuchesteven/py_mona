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

bob = db.get(Author, 1)

all_authors = db.all(Author)
print(all_authors)
post = Post(title="Hello, World!", published=True, author=author)

db.save(post)

print(db.get(Post, 1).author)

for author in all_authors:
    print(author.name)
    print(author.lucky_number)
if __name__ == '__main__':
    print('This is mona, a cross platform ORM for Python.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
