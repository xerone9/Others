import PIL
from PIL import Image
import os

input_directory = r'D:\Fee Silps 2014\\'
output_directory = r'D:\PATH\\'
c = 0

left_cut = [566.6666666666666, 283.3333333333333, 0, 0]
top_cut = [292.5, 292.5, 320, 0]
right_cut = [850, 566.6700000000001, 283.3333333333333, 850]
bottom_cut = [1170, 1170, 1170, 350]

for filename in os.listdir(input_directory):
    if filename.endswith(".jpg"):
        list = str(filename).split(",")
        substr = ".jpg"
        if any(substr in str for str in list):
            list.pop(-1)
        else:
            pass

        c = 0
        for values in list:
            sub_name = values.replace(" ","").replace(".jpg", "")

            im = Image.open(input_directory + filename)
            width, height = im.size

            # a = 0
            # b = 0
            # c = 283.33
            # d = 0
            #
            # left = 0
            # top = 0
            # right = 850
            # bottom = 350

            try:
                im1 = im.crop((left_cut[c], top_cut[c], right_cut[c], bottom_cut[c]))
                if c == 3:
                    im1 = im1.rotate(90, PIL.Image.NEAREST, expand = 1)

                # Shows the image in image viewer

                    im1 = im1.save(output_directory + sub_name + ".jpg")
                    c += 1
                    # print(values + ".jpg")
                else:

                    im1 = im1.save(output_directory + sub_name + ".jpg")
                    c += 1
                    # print(values + ".jpg")
            except IndexError:
                print(filename + " <-- This File has an issue")