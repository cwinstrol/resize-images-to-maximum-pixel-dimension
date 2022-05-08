#overwrites files

import os
from PIL import Image
from PIL import ImageOps
#dir=''
def imgs_resize():
    for p,ds,fs in os.walk(dir):
        for f in fs:
            if f.endswith(('jpg','jpeg' or 'png')):
                with Image.open(p+'\\'+f) as image:
                    w,h=image.size
                    if w>1440 or h>1440:
                        if (w>h):
                            nw=1440
                            nh=int(h/w*1440)
                            image=image.resize((nw,nh),Image.ANTIALIAS)
                        else:
                            nw=int(w/h*1440)
                            nh=1440
                            image=image.resize((nw,nh),Image.ANTIALIAS)
                    image=ImageOps.exif_transpose(image)
                    image.save(p+'\\'+f,quality=40,optimize=True)
