import os
import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

def create_pdf(input_folder, output_pdf, crop_area, file_extension):
    # Get a sorted list of image files in the folder
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(file_extension)])

    # Create a PDF from the cropped images
    c = canvas.Canvas(output_pdf, pagesize=A4)
    a4_width, a4_height = A4

    for filename in image_files:
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            cropped_img = img.crop(crop_area)

            img_width, img_height = cropped_img.size

            # Calculate the scaling factor to fit the image within A4 dimensions
            scale_factor = min(a4_width / img_width, a4_height / img_height)
            scaled_width = img_width * scale_factor
            scaled_height = img_height * scale_factor

            # Use ImageReader to draw the image directly from the Pillow object
            image_reader = ImageReader(cropped_img)
            c.drawImage(image_reader, 0, a4_height - scaled_height, width=scaled_width, height=scaled_height)
            c.showPage()

    c.save()
    print(f"PDF created successfully at {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop images and create a PDF.")
    parser.add_argument("input_folder", type=str, help="Folder containing the images.")
    parser.add_argument("output_pdf", type=str, help="Output PDF file path.")
    parser.add_argument("crop_area", type=int, nargs=4, help="Crop area as four integers: left, upper, right, lower.")
    parser.add_argument("--file_extension", type=str, default=".png", help="Image file extension (default: .png)")

    args = parser.parse_args()
    create_pdf(args.input_folder, args.output_pdf, tuple(args.crop_area), args.file_extension)