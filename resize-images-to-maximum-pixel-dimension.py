#dn=''
def imgs_resize(dn):
    for p,ds,fs in os.walk(dn):
        p=os.path.join(p,'')
        if p.endswith('ir\\'):
            for f in fs:
                with Image.open(os.path.join(p+f)) as image:
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
                    image.save(p[:-3]+f,quality=40,optimize=True)
