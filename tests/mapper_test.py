import unittest

DB_PATH = '../test.db'


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
        pass


class MapperTest4_CreateForeignKey(unittest.TestCase):
    def test_create_foreign_key(self):
        pass


class MapperTest5_SaveInstance(unittest.TestCase):
    def test_save_instance(self):
        pass


class MapperTest6_GetInstance(unittest.TestCase):
    def test_get_instance(self):
        pass


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
