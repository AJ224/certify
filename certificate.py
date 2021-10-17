import streamlit as st

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
st.title("Certificate Provider")

img = Image.open("certificate.png")
st.sidebar.title("Certificates")
st.sidebar.image("certificate.png")
#Adjust you y-coordinate here
y_coordinate = 656

name = st.text_input('\nYour name : ')
text= st.text_area("Text You Want On Certificate")
para= textwrap.wrap(text, width=40)

width, height = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("j.ttf", 90)
font1 = ImageFont.truetype("j.ttf", 45)
offset = 10
x_coordinate = int(width / 2 - font.getsize(name)[0] / 2) + offset
draw.text((x_coordinate, y_coordinate), name, (255, 0, 0), font=font)
max_w, max_h=1592,100
current_h, pad= 841,10
for line in para:
    w,h= draw.textsize(line, font=font1)
    draw.text(((max_w-w)/2, current_h),line,(200,0,0), font=font1)
    current_h += h+pad
#draw.text((x_coordinate, y_coordinate), text, (255, 0, 0), font=font)
#draw.text((x_coordinate, 800), text, (255, 0, 0), font=font1)

#img.save(str(name) + ".png", "PNG")
st.image(img)