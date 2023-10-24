
def main():
  myList = ["AB", "CD"]
  print(myList)

  print()
  myList.append("EF")
  print(myList)

  print()
  myList[0] += "12"
  print(myList)

  print()
  myList = []
  print(myList)

  print()
  myList.append("AB")
  print(myList)

  print()
  myList = []
  for c in myList:
    print(c)

  print()
  myList.append("")
  myList[0] += "12"
  # myList[2] += "1" # out of range
  print(myList)


if __name__ == "__main__":
  main()
else:
  pass