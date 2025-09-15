"""
    Demonstrates using PyMuPDF and Pillow to extract and display
    an image from a pdf file.
"""

import fitz         #   module name for PyMuPDF
import PIL.Image    # pillow
import io           #   input output

pdf = fitz.open("./res/test.pdf")
counter = 1         #   counts the images

#   for each pdf page
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        #   The base_image is a dictionary with the metadata of the image
        #   including the bytes of the image
        base_image = pdf.extract_image(image[0])
        image_data = base_image['image']
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_image['ext']
        img.save(open(f"output_image{counter}.{extension}", "wb"))
        counter += 1