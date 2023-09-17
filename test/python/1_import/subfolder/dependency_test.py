
def funcNotImported():
  return 1

def funcWithDependency():
  return funcNotImported()
