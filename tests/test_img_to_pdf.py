import os
import pytest
from PIL import Image
from img_to_pdf.__main__ import create_pdf

@pytest.fixture
def setup_test_environment(tmp_path):
    # Create a temporary directory and some test images
    test_dir = tmp_path / "test_images"
    test_dir.mkdir()
    for i in range(3):
        img = Image.new('RGB', (3000, 3000), color = (i * 50, i * 50, i * 50))
        img.save(test_dir / f"test_image_{i}.png")
    return test_dir

def test_create_pdf(setup_test_environment, tmp_path):
    input_folder = setup_test_environment
    output_pdf = tmp_path / "output.pdf"
    crop_area = (1000, 1000, 2000, 2000)
    file_extension = ".png"

    create_pdf(str(input_folder), str(output_pdf), crop_area, file_extension)

    assert os.path.exists(output_pdf)
    # Additional checks can be added to verify the content of the PDF
