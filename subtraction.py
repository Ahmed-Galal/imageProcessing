from PIL import Image
from numpy import *

im1 = Image.open('Smooth.jpg')
im2 = Image.open('Sharpen.jpg')

im1arr = asarray(im1)
im2arr = asarray(im2)

sub = im1arr - im2arr

resultImage = Image.fromarray(sub)
resultImage.save('subtracted.jpg')

