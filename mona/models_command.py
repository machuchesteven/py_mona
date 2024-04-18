import os
import inspect
import sys
import importlib
from mapper import Table


class BaseCommand:
    def __init__(self, client, **kwargs):
        self.client = client
        self.kwargs = kwargs

    def run(self):
        '''Here creates a run server command for This project'''
        raise NotImplementedError

    def migrate(self):
        '''Here creates a migrate command for This project'''
        filename = 'models'
        module = importlib.import_module(f'{filename}')
        classes = inspect.getmembers(module, inspect.isclass)
        for name, cls in classes:
            if issubclass(cls, Table):
                print(cls._get_name())
        print("All classes listed above and migrations were created successfully.")

    def new(self):
        '''Here creates a new project command for This project'''
        raise NotImplementedError


if __name__ == "__main__":
    base = BaseCommand('mona')
    base.migrate()
    print("Completed")