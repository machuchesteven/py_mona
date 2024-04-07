from setuptools import setup, find_packages
import os

# metadata
VERSION = '1.0.0'
DESCRIPTION = 'A simple ORM for SQLite3'
LONG_DESCRIPTION = '''A SIMPLE ORM FOR SQLITE3 DATABASES IN PYTHON 3 Mona is a simple ORM for SQLite3 databases in 
    Python 3. It is designed to be simple and easy to use. It is not meant to be a full-featured ORM like SQLAlchemy, 
    but rather a simple and easy-to-use ORM for small projects.'''

# setting up
setup(
    name='mona',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Mona Developer',
    author_email='machuchesteven@gmail.com',
    long_description_content_type='text/markdown',
    keywords=['ORM', 'database', 'sqlite'],
    install_requires=[],
    packages=find_packages(),
    classifiers=[
        'Development Status ::  1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent'
    ]
)
