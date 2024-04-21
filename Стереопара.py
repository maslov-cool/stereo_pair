from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    pixels = im.load()
    x, y = im.size
    new_im = Image.new('RGB', (x, y), (0, 0, 0))
    new_pixels = new_im.load()
    for i in range(delta, x):
        for j in range(y):
            r, g, b = pixels[i, j]
            r1, g1, b1 = pixels[i - delta, j]
            new_pixels[i, j] = r1, g, b
    for i in range(delta):
        for j in range(y):
            r, g, b = pixels[i, j]
            new_pixels[i, j] = 0, g, b
    new_im.save('res.jpg')


makeanagliph("image.jpg", 20)


