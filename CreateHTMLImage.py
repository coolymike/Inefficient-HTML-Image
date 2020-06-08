from PIL import Image
import random

im = Image.open("Yalikejazz.jpg")
randomize = True
Scale = 1

HTML = ""
finalCSS = ""
width, height = im.size
for x in range(width):
    for y in range(height):
        r, g, b = im.getpixel((x,y))
        a = 255
        HTML += f"<div id=x{x}y{y}></div>\n"
        finalCSS += f"#x{x}y{y}" + "{ " + f"position:absolute; top:{y * Scale}px; left:{x * Scale}px; width:{Scale}px; height:{Scale}px; background-color:rgba({r}, {g}, {b}, {a / 255})" + " }\n"

if randomize:
    HTML = HTML.split("\n")
    random.shuffle(HTML)
    HTML = "\n".join(HTML)

FinalHTML = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Image</title>
  <style>
{finalCSS}
  </style>
</head>
<body>
{HTML}
</body>
</html>"""

with open("HTMLImage.html", "w+") as f:
    f.write(FinalHTML)
