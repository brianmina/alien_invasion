from PIL import Image
from PIL import ImageColor

im = Image.open('mario.bmp')
newIm = im.resize((50, 50))
newIm.save("ship_smaller_mario.bmp")
#newIm_yoshi = Image.new("RGBA",(20,20))
#im.paste(newIm)
#im.save("new_yoshiiii.bmp")



