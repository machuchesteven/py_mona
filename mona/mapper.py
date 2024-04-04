import sqlite3
import os
import inspect

SQLITE_TYPES = {
    int: 'INTEGER',
    str: 'TEXT',
    float: 'REAL',
    bool: 'BOOLEAN',
    bytes: 'BLOB'
}
CREATE_TABLE_SQL = 'CREATE TABLE {name} ({fields});'
SELECT_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type='table';"
INSERT_SQL = 'INSERT INTO {name} ({fields}) VALUES ({values});'
SELECT_ALL_SQL = 'SELECT {fields} FROM {name};'
SELECT_ONE_SQL = 'SELECT {fields} FROM {name} WHERE id = ?;'
DELETE_SQL = 'DELETE FROM {name} WHERE id = ?;'
UPDATE_SQL = 'UPDATE {name} SET {fields} WHERE id = ?;'
class Database:
    '''
    Database class to handle all database operations. All other instances
    will be inherited from this parent class
    '''
    def __init__(self, path:str|None=None):
        if path is not None:
            self.conn = sqlite3.Connection(path)

    @property
    def tables(self):
        return [row[0] for row in self._execute(SELECT_TABLES_SQL).fetchall()]

    def _execute(self, sql, params=None):
        '''
        Execute a SQL command
        '''
        if params:
            return self.conn.execute(sql, params)
        return self.conn.execute(sql)


    def create(self, table):
        '''Create a new instance of a table in the database'''
        self._execute(table._get_create_sql())

    def save(self, instance):
        '''Save a new instance of a defined object into a table'''
        sql , values = instance._get_insert_sql()
        cursor = self._execute(sql, values)
        instance._data['id'] = cursor.lastrowid

    @classmethod
    def get(cls, obj:object, id:int):
        '''
        Retrieves a single instance of a defined object from a table
        '''
        pass
    @classmethod
    def delete(cls, obj:object, id:int):
        '''Deletes a single instance of an object from a table defined'''
        pass
    @classmethod
    def all(cls, obj:object):
        '''Returns all instances of an object from a table defined'''
        pass


class Table:
    def __init__(self, **kwargs):
        self._data = {
            'id': None
        }
        for key, value in kwargs.items():
            self._data[key] = value

    def __getattribute__(self, key):
        _data = object.__getattribute__(self, '_data')
        if key in _data:
            return _data[key]
        return object.__getattribute__(self, key)

    def _get_insert_sql(self) -> str:
        fields = []
        values = []
        placeholders = []
        for name, field in inspect.getmembers(self.__class__):
            if isinstance(field, Column):
                fields.append(name)
                values.append(getattr(self, name))
                placeholders.append('?')
            if isinstance(field, ForeignKey):
                fields.append(f'{name}_id')
                values.append(getattr(self, name).id)
                placeholders.append('?')

        sql =  INSERT_SQL.format(name=self.__class__._get_name(),
                                 fields=[], values=[])
        return sql

    @classmethod
    def _get_name(cls):
        return cls.__name__.lower()

    @classmethod
    def _get_create_sql(cls):
        fields = [
            ("id", "INTEGER PRIMARY KEY AUTOINCREMENT")
        ]
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append((name, field.sql_type))
            if isinstance(field, ForeignKey):
                fields.append((f'{name}_id', 'INTEGER'))
        fields = [" ".join(f) for f in fields]
        return CREATE_TABLE_SQL.format(name=cls._get_name(), fields=', '.join(fields))


class Column:
    def __init__(self, dt_type):
        self.dt_type = dt_type

    @property
    def sql_type(self):
        return SQLITE_TYPES[self.dt_type]

class ForeignKey:
    def __init__(self, table):
        self.table = table


