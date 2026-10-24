# Genera resources/icon.png y resources/splash.png (lo corre GitHub al compilar)
import os
from PIL import Image, ImageDraw
os.makedirs('resources', exist_ok=True)
S=1024; R=(201,54,42); im=Image.new('RGB',(S,S),R); d=ImageDraw.Draw(im)
# barra con discos, estilo pesa olímpica
d.rounded_rectangle([180,488,844,536],radius=20,fill=(240,240,240))
for x,w,h,c in [(300,70,360,(30,93,186)),(380,50,280,(217,154,0)),(644,50,280,(217,154,0)),(724,70,360,(30,93,186))]:
    d.rounded_rectangle([x-w//2+ (0 if x<512 else 0),512-h//2,x+w//2,512+h//2],radius=18,fill=c)
im.save('resources/icon.png')
Image.new('RGB',(2732,2732),R).save('resources/splash.png')
print('iconos listos')
