import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
import random

from PIL import Image


square_size = 10
offset_factor = 20
darken_factor = 0.1

image = Image.open("image.jpg")
size = image.size

# Create image np array
im = np.array(image, dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Add random offset to tuple based on offset_factor
def add_offet(t):
    t[0] = random.randint(t[0], (t[0] + offset_factor))
    t[1] = random.randint(t[1], (t[1] + offset_factor))

    return t


# Create a Rectangle patch
for w in xrange(0, size[0], square_size):
    for h in xrange(0, size[1], square_size):
        print str(w) + ':' + str(h)

        # Get the average color of the section
        rect = im[h:h+square_size, w:w+square_size]
        mean = rect.mean(axis=(0,1))

        # Convert to hex value
        face_color = '#%02x%02x%02x' % (int(mean[0]), int(mean[1]), int(mean[2]))
        edge_color = '#%02x%02x%02x' % (int(mean[0] - (mean[0] * darken_factor)), int(mean[1]  - (mean[1] * darken_factor)), int(mean[2] - (mean[2] * darken_factor)))

        # Dont draw outline with the dominant color
        z_order = 2
        if '#e' in face_color or '#f' in face_color:
            line_width = 0.0
        else:
            line_width = 0.1
            z_order = 3

        points = [add_offet([w, h]), add_offet([w + square_size, h]), add_offet([w, h + square_size])]
        triangle1 = patches.Polygon(points, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Second triangle
        points2 = [add_offet([w, h + square_size]), add_offet([w + square_size, h + square_size]), add_offet([w + square_size, h])]
        triangle2 = patches.Polygon(points2, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Square in background
        rec = patches.Rectangle((w,h),square_size,square_size,linewidth=0.0, edgecolor=edge_color, facecolor=face_color, zorder=1)

        # Add the patch to the Axes
        ax.add_patch(triangle1)
        ax.add_patch(triangle2)
        ax.add_patch(rec)


plt.axis('off')
plt.savefig("out.png", bbox_inches='tight', dpi=2048)
# plt.show()
