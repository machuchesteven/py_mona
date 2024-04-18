from mapper import Table, Column, ForeignKey, Database


class Author(Table):
    name = Column(str)
    lucky_number = Column(int)


class Post(Table):
    title = Column(str)
    published = Column(bool)