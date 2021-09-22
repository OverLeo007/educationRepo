from PIL import Image, ImageDraw


def ph(n):
    # n = 256
    wars = list(range(1, n + 1))
    while len(wars) != 1:
        del wars[::3]
    return wars[0]


def to_255(n):
    return n % 255


# Создаем белый квадрат
rzr = tuple(map(int, input().split()))
img = Image.new('RGBA', rzr, 'black')
idraw = ImageDraw.Draw(img)
rect_len, rect_hei = rzr[0] // 10, rzr[1] // 10

for i in range(0, rzr[0] + rect_len, rect_len):
    for j in range(0, rzr[1] + rect_hei, rect_hei):
        # print(i % 255, j % 255, (i + j) // 2 % 255)
        print(i, j, rect_len, rect_hei)
        idraw.rectangle((i, j, rect_len, rect_hei), fill=(i % 255, j % 255, (i + j) // 2 % 255))

img.save('rectangle.png')
