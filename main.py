# ------------------------------------------- Imports -------------------------------------------
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ------------------------------------------- Open The Colored Image -------------------------------------------
colored_img = Image.open("sao-paulo.png")
colored_img_array = np.array(colored_img)
grey_vals = np.array([0.2126/255, 0.7152/255, 0.0722/255])

# ------------------------------------------- Convert to Black and White Image -------------------------------------------
gray_img_array = colored_img_array @ grey_vals # Multiply the colored array to get the gray array tuple values

# ------------------------------------------- Display the Black and White Image -------------------------------------------
plt.imshow(gray_img_array, cmap='gray')
plt.savefig('gray.jpg') # Save the image
plt.show()
