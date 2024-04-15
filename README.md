# Mona ORM

a python Object Relational Mapper (ORM) that aims to focus on concurrency
and performance.

## Usage Direction

1. Install the package using pip
```bash
pip install mona-orm
```
2. Create a new project using the command line tool
```bash
mona-orm new project_name
```
3. Edit the `settings.py` file to configure the database connection
4. Create a new model using the command line tool
```bash
mona-orm model model_name
```
5. Edit the model file to define the fields
6. Run the migrations to create the table in the database
```bash
mona-orm migrate
```
7. Use the model in your code
```python
from mona.mapper import Table,Column, ForeignKey

# Create a new instance of the model
class YourModel(Table):
    id = Column(primary_key=True)
    name = Column(str, unique=True)
    age = Column(int)
    address = Column(str, length=None, max_length=number, ...)
    # Define the relationships
    # user_id = Column(ForeignKey('user.id'))
```
8. Run the project
```bash
mona-orm run
```
9. Enjoy the ORM
10. Contribute to the project

## Projects Architecture

## Columns Configuration and arguments
Table columns which are treated as model fields can be configured based on the type of the field and on the desired attributes. The following are the available column types and their arguments:-

## Creating Views

## Dealing with Asynchronous Code

## Contributing to the project

## License


## About the Author
