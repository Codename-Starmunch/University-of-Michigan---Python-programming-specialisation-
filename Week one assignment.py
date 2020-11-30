import PIL
from PIL import Image
from PIL import ImageFont, ImageDraw
from PIL import ImageEnhance

image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

images = []
text = []

image_hues = 0.1, 0.5, 0.9

for i in range(3):
    for k in image_hues:
        base = image.split()
        adj = base[i].point(lambda x: x * k)
        base[i].paste(adj)
        blend = Image.merge(image.mode, base)
        text.append(f'channel {i} intensity {k}')
        images.append(blend)

first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3 + 3 * 50))

x = 0
y = 0

draw = ImageDraw.Draw(contact_sheet)

for i, img in enumerate(images):
    contact_sheet.paste(img, (x, y))
    draw.text((x, y + first_image.height + 5), text[i], font=ImageFont.truetype("readonly/fanwood-webfont.ttf", 60))

    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height + 50

    else:
        x = x + first_image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)