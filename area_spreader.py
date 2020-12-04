
from PIL import Image
import numpy as np
from typing import List, Tuple
from PIL import Image, ImageDraw
from numbers import Number




def create_tile_mask_img(tile_size: int, polygons: List[List[Tuple[Number, Number]]], boundary_px: int) -> Image:
    tile_image_array = np.full((tile_size, tile_size, 3), 0, dtype=np.uint8)
    original = Image.fromarray(tile_image_array, "RGB")
    draw: ImageDraw = ImageDraw.Draw(original)
    for xy in polygons:
        draw.polygon(xy, fill=(0, 100, 255), outline=(0, 0, 255))
        draw.line(xy, fill=(255, 255, 0), width=boundary_px)
        draw.line([xy[-1], xy[0]], fill=(255, 255, 0), width=boundary_px)
    return(original)


def create_tile_spread_img(tile_size: int, polygons: List[List[Tuple[Number, Number]]], boundary_px: int) -> Image:
    tile_image_array = np.full((tile_size, tile_size, 3), 0, dtype=np.uint8)
    original = Image.fromarray(tile_image_array, "RGB")
    draw: ImageDraw = ImageDraw.Draw(original)
    for xy in polygons:
        draw.polygon(xy, fill=(0, 100, 255), outline=(0, 0, 255))
        draw.line(xy, fill=(255, 255, 0), width=boundary_px)
        draw.line([xy[-1], xy[0]], fill=(255, 255, 0), width=boundary_px)
    return(original)


poly1 = [(25,25),(111,15),(185,46),(191,94),(166,124),(141,164),(132,214),(149,264),(191,292),(216,345),(180,450),(46,444),(48,225)]
poly2 = [(294,46),(433,43),(478,111),(421,150),(315,227),(208,132)]
poly3 = [(379,378),(440,367),(406,416),(372,400)]
size = 600
img = create_tile_mask_img(tile_size=size, polygons=[poly1,poly2,poly3], boundary_px=1)
img.show()