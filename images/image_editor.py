from PIL import Image
from PIL import ImageColor

im = Image.open('yoshi-5994957_640.png')
newIm = im.resize((50, 50))
newIm.save("new_yoshi.bmp")
#newIm_yoshi = Image.new("RGBA",(20,20))
#im.paste(newIm)
#im.save("new_yoshiiii.bmp")



