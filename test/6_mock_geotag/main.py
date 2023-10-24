

from PIL import Image
import piexif

def main():
  img = Image.open("inp.jpg")
  # exif_dict = piexif.load(img.info["exif"])

if __name__ == "__main__":
  main()
else:
  pass