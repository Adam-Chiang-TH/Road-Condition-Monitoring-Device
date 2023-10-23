import time


def waitForUnixEpoch():
  ret = 0
  while ret == 0:
    ret = time.time()
  return ret

def main():
  t1 = waitForUnixEpoch()
  folderName = time.strftime("%Y-%m-%d_%H-%M-%S")
  print(folderName)

  print()
  while True:
    if time.time() - t1 >= 0.25: # 0.25 for 4 Hz
      t1 = time.time()
      print(t1)

if __name__ == "__main__":
    main()
else:
    pass