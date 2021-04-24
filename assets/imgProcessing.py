import os
from PIL import Image
import numpy as np

for path in os.listdir("players"):
    if path != ".DS_Store":
        temp = Image.open("players/" + path)
        temp = temp.resize((70, 150))



        image_data = temp.load()

        height, width = temp.size


        temp = temp.convert('RGBA')
        data = np.array(temp)
        # just use the rgb values for comparison
        rgb = data[:, :, :3]
        color = [52,72, 93]  # Original value
        black = [0, 0, 0, 255]
        white = [255, 255, 255, 255]

        mask = np.all(rgb == color, -1)
        # change all pixels that match color to white
        data[mask] = white

        # change all pixels that don't match color to black
        ##data[np.logical_not(mask)] = black
        new_im = Image.fromarray(data)
        new_im.save('new_file.tif')


rgb(52,72,93)


