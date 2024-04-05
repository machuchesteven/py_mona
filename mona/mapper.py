import sqlite3
import os
import inspect
from typing import Tuple, List, Any

SQLITE_TYPES = {
    int: 'INTEGER',
    str: 'TEXT',
    float: 'REAL',
    bool: 'BOOLEAN',
    bytes: 'BLOB'
}
CREATE_TABLE_SQL = 'CREATE TABLE {name} ({fields});'

SELECT_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type='table';"

INSERT_SQL = 'INSERT INTO {name} ({fields}) VALUES ({placeholders});'

SELECT_ALL_SQL = 'SELECT {fields} FROM {name};'

SELECT_ONE_SQL = 'SELECT {fields} FROM {name} WHERE id = ?;'

DELETE_SQL = 'DELETE FROM {name} WHERE id = ?;'

UPDATE_SQL = 'UPDATE {name} SET {fields} WHERE id = ?;'

SELECT_WHERE_SQL = 'SELECT {fields} FROM {name} WHERE {conditions};'

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
        sql, values = instance._get_insert_sql()
        cursor = self._execute(sql, values)
        instance._data['id'] = cursor.lastrowid


    @classmethod
    def delete(cls, obj:object, id:int):
        '''Deletes a single instance of an object from a table defined'''
        pass

    def all(self, table):
        '''Returns all instances of an object from a table defined'''
        sql, fields = table._get_select_all_sql()
        result = []
        for row in self._execute(sql).fetchall():
            data = dict(zip(fields, row))
            result.append(table(**data))
        return result

    def get(self, table, id: int):
        '''
        Retrieves a single instance of a defined object from a table
        '''
        sql, fields, params = table._get_select_where_sql(id=id)
        row = self._execute(sql, params=params).fetchone()
        data = dict(zip(fields, row))
        return table(**data)

    def get(self, table, **kwargs):
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

    def _get_insert_sql(self) -> tuple[str, list[Any]]:
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

        sql = INSERT_SQL.format(name=self.__class__._get_name(),
                                 fields=', '.join(fields),
                                 placeholders=', '.join(placeholders))
        return sql, values

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

    @classmethod
    def _get_select_all_sql(cls):
        fields = ['id']
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            if isinstance(field, ForeignKey):
                fields.append(f'{name}_id')
        fields = ', '.join(fields)
        return SELECT_ALL_SQL.format(name=cls._get_name(), fields=fields), fields

    @classmethod
    def _get_select_where_sql_by_id(cls, id:int):
        fields = ['id']
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            if isinstance(field, ForeignKey):
                fields.append(f'{name}_id')
        conditions = 'id = ?'
        fields = ', '.join(fields)

        return SELECT_WHERE_SQL.format(name=cls._get_name(), fields=fields, conditions=conditions), fields, id

    @classmethod
    def _get_select_where_sql(cls, **kwargs):
        fields = ['id']
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            if isinstance(field, ForeignKey):
                fields.append(f'{name}_id')
        conditions = ' AND '.join([f'{key} = ?' for key in kwargs.keys()])
        sql = SELECT_WHERE_SQL.format(name=cls._get_name(), fields=', '.join(fields), conditions=conditions)
        return sql, fields, list(kwargs.values()), fields, conditions


class Column:
    def __init__(self, dt_type):
        self.dt_type = dt_type

    @property
    def sql_type(self):
        return SQLITE_TYPES[self.dt_type]

class ForeignKey:
    def __init__(self, table):
        self.table = table


