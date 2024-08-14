from mona.mapper import Table, Database, Column

def main():
    db = Database("my_try.db")
    print(db.tables)

    class Post(Table):
        title = Column(str)
        content = Column(str)

    class Author(Table):
        name = Column(str)
        age = Column(int)

    db.create(Post)
    db.create(Author)

    print(db.tables)
    print(Post.__name__)

    author = Author(name="John Doe", age=30)
    db.save(author)

    post = Post(title="Hello, World!", content="This is a test post")
    db.save(post)

    print(db.all(Author))
    print(db.all(Post))

    author = db.get(Author, 1)
    print(author.name)

if __name__ == "__main__":
    main()