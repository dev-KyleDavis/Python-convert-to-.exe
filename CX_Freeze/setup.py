from cx_Freeze import setup, Executable

setup(name='enter name of program here',
      version='1.0',
      description='By: K. Davis 2023',
      executables=[Executable('python file name here.py')])

# run this command in the cmd - "python setup.py build"