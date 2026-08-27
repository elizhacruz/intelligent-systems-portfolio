from io import BytesIO
import os
import piexif
import requests
from PIL import Image

image_url = "https://www.maxfosterphotography.com/images/xl/Rise-Above.jpg"
image_filename = "sample.jpg"


def download_sample_image():
  print(f"Downloading sample image from {image_url}...")
  response = requests.get(image_url)
  with open(image_filename, "wb") as f:
    f.write(response.content)


def analyze_exif():
  if not os.path.exists(image_filename):
    download_sample_image()

  print("\nEXIF Metadata Analysis:")
  try:
    img = Image.open(image_filename)
    exif_data = piexif.load(img.info.get("exif", b""))

    ifth_data = exif_data.get("0th", {})
    make = ifth_data.get(piexif.ImageIFD.Make, b"Unknown").decode(
        "utf-8", errors="ignore"
    )
    model = ifth_data.get(piexif.ImageIFD.Model, b"Unknown").decode(
        "utf-8", errors="ignore"
    )

    exif_ifd = exif_data.get("Exif", {})
    date_time = exif_ifd.get(piexif.ExifIFD.DateTimeOriginal, b"Unknown").decode(
        "utf-8", errors="ignore"
    )

    print(f"Camera Make: {make.strip('\x00')}")
    print(f"Camera Model: {model.strip('\x00')}")
    print(f"Date/Time Original: {date_time.strip('\x00')}")

  except Exception as e:
    print(f"Error reading EXIF data: {e}")


if __name__ == "__main__":
  analyze_exif()