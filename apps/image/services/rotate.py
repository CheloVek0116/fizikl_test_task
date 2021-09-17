from io import BytesIO

from django.core.files import File
from PIL import Image


def flip_image(file_image) -> File:
    return rotate_image(file_image, 180)


def rotate_image(file_image, degrees) -> File:
    new_image = BytesIO()
    pil_image = Image.open(file_image)
    new_pil_image = pil_image.rotate(degrees, expand=True)
    new_pil_image.save(new_image, pil_image.format)
    new_image.seek(0)
    return File(new_image)
