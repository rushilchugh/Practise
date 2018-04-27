__author__ = 'Rushil'

from PIL import Image
import numpy as np

img = Image.open(r'C:\NOS\Coding\Puzzles\Images\index.jpg' , 'r')
img = np.array(img)

img = Image.fromarray(img[::2 , ::2])
img.save(r'C:\NOS\Coding\Puzzles\Images\img.jpg')