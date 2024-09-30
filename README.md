# img_to_pdf

img_to_pdf is a tool to crop images and create a PDF. This package is not available on PyPI and can be installed via GitHub.

## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/docs/):

```sh
git clone https://github.com/hemangsk/img_to_pdf.git
cd img_to_pdf
poetry install
```

## Usage

Run the script with the required arguments:

```sh
poetry run python -m img_to_pdf <input_folder> <output_pdf> <left> <upper> <right> <lower> [--file_extension <file_extension>]
```

### Arguments

| Argument         | Description                                      | Example                          |
|------------------|--------------------------------------------------|----------------------------------|
| `input_folder`   | Folder containing the images                     | `/Users/hemang/Desktop/murga/`   |
| `output_pdf`     | Output PDF file path                             | `/Users/hemang/Desktop/output.pdf`|
| `left`           | Left coordinate of the crop area                 | `1000`                           |
| `upper`          | Upper coordinate of the crop area                | `20`                             |
| `right`          | Right coordinate of the crop area                | `2450`                           |
| `lower`          | Lower coordinate of the crop area                | `2080`                           |
| `file_extension` | Image file extension (default: `.png`)           | `.jpg`                           |

### How to Obtain/Calculate Crop Area

To determine the pixel values for cropping, you can use an image viewer or editor that allows you to see the pixel coordinates. Here are a few methods:

1. **Using an Image Editor (e.g., Photoshop, GIMP)**
   - Open the image in an editor.
   - Use the crop tool to select the area you want to crop.
   - Note the coordinates of the selected area.

2. **Using Python and Pillow**
   - Write a small script to display the image and manually inspect the coordinates.

```python
from PIL import Image

# Open an image file
img_path = '/path/to/your/image.png'
with Image.open(img_path) as img:
    img.show()  # This will open the image in the default image viewer

# Print image size
print(f"Image size: {img.size}")  # This will print the (width, height) of the image
```

3. **Using a GUI Tool (e.g., `matplotlib`)**
   - Use `matplotlib` to display the image and manually inspect the coordinates.

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display the image
img_path = '/path/to/your/image.png'
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)
plt.show()
```

## Example

```sh
poetry run python -m img_to_pdf /Users/hemang/Desktop/murga/ /Users/hemang/Desktop/output.pdf 1000 20 2450 2080 --file_extension .jpg
```

## Running Tests

To run the tests, use the following command:

```sh
poetry run pytest
```