import imported
from imported import func2
from imported import func4 as f

# import subfolder.imported as imported # legal, but overwrites the previously-imported module
import subfolder.imported # run functions from this module using its full name (e.g. subfolder.imported.func1())

from subfolder.dependency_test import funcWithDependency

def main():
  print("main() is run! __name__ = " + __name__ +"\n")

  print("imported.func1():", imported.func1())
  print(f"imported.func1(): {imported.func1()}") # fstring method
  # print("imported.func1(): " + imported.func1()) # TypeError: can only concatenate str (not "float") to str
  print("imported.func2():", imported.func2())
  print("imported.func2(): " + imported.func2()) # legal because + is concatenation and func2() returns str

  print("\n" + "func2():", func2())

  # print("\n" + "func3():", func3()) # NameError: name 'func3' is not defined
  print("\n" + "imported.func3():", imported.func3())

  print("\n" + "f():", f())
  # print("\n" + "func4():", func4()) # NameError: name 'func4' is not defined

  print("\n" + "subfolder.imported.func1():", subfolder.imported.func1())

  print("\n" + "subfolder.dependency_test.funcWithDependency():", subfolder.dependency_test.funcWithDependency()) # can also be run like this
  print("funcWithDependency():", funcWithDependency())
  # print("funcWithDependency(): " + funcWithDependency()) # TypeError: can only concatenate str (not "int") to str

  print()

if __name__ == "__main__":
  main()
else:
  pass