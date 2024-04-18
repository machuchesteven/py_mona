import sys
import os

PROJECT_NAME = ''
IS_API_ONLY = False
USE_DATABASE = True
# check if configuration arguments are provided during the time of initialization of the project

# check if the command is for initialization of a new project

def create_db_settings():
    '''
    This creates a settings python file whenever a module to create a
    a python project using the MONA ORM is issued.
    This is the file used to store the database settings.
    '''
    with open(os.path.join(os.getcwd(), 'settings.py'), 'w') as f:
        f.write('import os\n')
        f.write('# Here goes your settings for accessing the database for your project.\n')
        f.write('DB_PATH = "test.db"\nDB_PATH = "test.db"\nDB_NAME = "test"\nDB_USER = "root"\n')
        f.write('DB_PASSWORD = "root"\nDB_HOST = "localhost"\nDB_PORT = 3306 \n\n')
        f.write("# You can add other modules here which you can access using the settings module.\n")


def create_folders(name:str):
    '''
    This creates a folder the project you initialize with a name.
    The folder structure is determined with the README.md file.
    '''
    os.mkdir(name)
    os.chdir(name)
    os.mkdir('tests')
    os.mkdir('models')
    os.mkdir('migrations')
    os.mkdir('controllers')
    os.mkdir('views')
    os.mkdir('static')
    os.mkdir('templates')
    os.mkdir('docs')
    return os.path.join(os.getcwd(), name)

def create_env_file(name:str):
    '''
    This creates an env file for the project.
    '''
    with open(os.path.join(os.getcwd(), name, '.env'), 'w') as f:
        f.write('DEBUG=True\n')
        f.write('SECRET_KEY=your_secret_key_here\n')
        f.write('DATABASE_URL=sqlite:///db.sqlite3\n')
        f.write('ALLOWED_HOSTS="*"\n')
        f.write('FILESERVER_URL=http://localhost:8000\n')
        f.write('FILESERVER_DIR=files\n')
        f.write('FILESERVER_PORT=8000\n')
    with open(os.path.join(os.getcwd(), name, '.dev.env'), 'w') as f:
        f.write('DEBUG=True\n')
        f.write('SECRET_KEY=your_secret_key_here')
        f.write('DATABASE_URL=sqlite:///db.sqlite3\n')
        f.write('ALLOWED_HOSTS="*"\n')
        f.write('FILESERVER_URL=http://localhost:8000\n')
        f.write('FILESERVER_DIR=files\n')
        f.write('FILESERVER_PORT=8000\n')


def create_readme_file(name:str):
    '''
    This creates a README.md file for the project.
    '''
    with open(os.path.join(os.getcwd(), name, 'README.md'), 'w') as f:
        f.write(f'# {name}\n')
        f.write('This is a simple project created using the MONA ORM.\n')
        f.write('## Installation\n')
        f.write('To install the project, run the following commands:\n')
        f.write('```bash\n')
        f.write(f'cd {name}\n')
        f.write('pip install -r requirements.txt\n')
        f.write('python manage.py runserver\n')
        f.write('```\n')
        f.write('## Usage\n')
        f.write('To use the project, run the following commands:\n')
        f.write('```bash\n')
        f.write('python manage.py runserver\n')
        f.write('```\n')
        f.write('## Contributing\n')
        f.write('To contribute to the project, follow the steps below:\n')


if __name__ == '__main__':
    print('This is mona, a cross platform ORM for Python.')
    if len(sys.argv) < 2:
        print('Please provide a command to run.')
        print('Usage: mona new <project_name>')
        sys.exit(1)
    if sys.argv[1] == 'new':
        project_name = sys.argv[2]
        create_folders(project_name)
        create_db_settings()
        print(f'Project {project_name} created successfully.')
        sys.exit(0)

    if sys.argv[1] == 'init':
        project_name = sys.argv[2]
        create_folders(project_name)
        create_db_settings()
        create_env_file(project_name)
        create_readme_file(project_name)
        print(f'Project {project_name} created successfully.')
        sys.exit(0)
    if sys.argv[1] == 'migrate':
        print('Migrating database...')
        sys.exit(0)
    if sys.argv[1] == 'run':
        print('Running server...')
        sys.exit(0)
