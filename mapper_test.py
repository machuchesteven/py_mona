import unittest

DB_PATH = 'test.db'


class MapperTest1_CreateDB(unittest.TestCase):

    def test_db_creation(self):
        global Database, db
        import os
        import sqlite3
        from mona.mapper import Database
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        db = Database(DB_PATH)
        assert isinstance(db.conn, sqlite3.Connection)
        assert db.tables == []


class MapperTest2_DefineTables(unittest.TestCase):

    def test_create_tables(self):
        from mona.mapper import Table, Database
        import os
        global Author, Post, db

        class Author(Table):
            pass

        class Post(Table):
            pass

        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        db = Database(DB_PATH)
        db.create(Author)
        db.create(Post)
        print(db.tables)
        assert Post.__name__ == 'Post'
        assert Author.__name__ == 'Author'
        assert db.tables == ['author', 'post']


class MapperTest3_CreateColumns(unittest.TestCase):
    def test_create_columns(self):
        from mona.mapper import Table, Database, Column
        import os
        global Author
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        db = Database(DB_PATH)

        class Author(Table):
            name = Column(str)
            age = Column(int)

        db.create(Author)
        assert db.tables == ['author']


class MapperTest4_CreateForeignKey(unittest.TestCase):
    def test_create_foreign_key(self):
        from mona.mapper import Table, Database, Column, ForeignKey
        import os
        global Author
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        db = Database(DB_PATH)

        class Author(Table):
            name = Column(str)
            age = Column(int)
        class Post(Table):
            author = ForeignKey(Author)
            title = Column(str)
            content = Column(str)
        db.create(Author)
        db.create(Post)
        assert db.tables == ['author', 'post']
class MapperTest5_SaveInstance(unittest.TestCase):
    def test_save_instance(self):
        from mona.mapper import Table, Database, Column, ForeignKey
        import os
        global Author
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        db = Database(DB_PATH)

        class Author(Table):
            name = Column(str)
            age = Column(int)

        class Post(Table):
            author = ForeignKey(Author)
            title = Column(str)
            content = Column(str)

        db.create(Author)
        db.create(Post)
        author = Author(name='John Doe', age=30)
        db.save(author)
        post = Post(author=author, title='Hello, World!', content='This is a test post')
        db.save(post)
        assert post.id == 1
        assert author.id == 1


class MapperTest6_GetInstance(unittest.TestCase):
    def test_get_instance(self):
        from mona.mapper import Table, Database, Column, ForeignKey
        import os
        global Author
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        db = Database(DB_PATH)

        class Author(Table):
            name = Column(str)
            age = Column(int)

        class Post(Table):
            author = ForeignKey(Author)
            title = Column(str)
            content = Column(str)

        db.create(Author)
        db.create(Post)
        author = Author(name='John Doe', age=30)
        db.save(author)
        auth = db.get(Author, id=author.id)
        print(auth.name)
        print(author.name)
        assert auth.name == author.name
        assert auth.age == author.age
        # post = Post(author=author, title='Hello, World!', content='This is a test post')
        # db.save(post)
        # post2 = db.get(Post, id=1)
        # assert post2.id == 1
        # assert post2.author.id == 1
        # assert post2.author.name == 'John Doe'
        # assert post2.author.age == 30


class MapperTest7_DeleteInstance(unittest.TestCase):
    def test_delete_instance(self):
        pass


class MapperTest8_AllInstances(unittest.TestCase):
    def test_all_instances(self):
        pass


class MapperTest9_UpdateInstance(unittest.TestCase):
    def test_update_instance(self):
        pass


class MapperTest10_UpdateTable(unittest.TestCase):
    def test_update_table(self):
        pass


if __name__ == '__main__':
    unittest.main()
