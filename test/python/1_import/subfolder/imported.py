print('subfolder/imported.py has been imported! __name__ = ' + __name__)

def func1():
  return 600

def func2():
  return 'abc' # same function name as another imported module, this "conflict" is ok