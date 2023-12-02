from PIL import Image
from PIL import ImageColor

im = Image.open('mario.bmp')
newIm = im.resize((100, 100))
newIm.save("ship_mario.bmp")
# newIm = Image.new("RGBA",(20,20))
# im.paste(newIm)

# im.save("mario_resize.bmp")



