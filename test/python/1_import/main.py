import imported
from imported import func2
from imported import func4 as f

# import subfolder.imported as imported # legal, but overwrites the previously-imported module
import subfolder.imported # run functions from this module using its full name (e.g. subfolder.imported.func1())

def main():
  print("main() is run! __name__ = " + __name__ +"\n")

  print(imported.func1())
  print(imported.func2())

  print(func2())

  # print(func3()) # NameError: name 'func3' is not defined
  print(imported.func3())

  print(f())
  # print(func4()) # NameError: name 'func4' is not defined

  print(subfolder.imported.func1())

if __name__ == '__main__':
  main()
else:
  pass