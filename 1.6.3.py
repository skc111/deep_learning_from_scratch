import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../check_board.png')
plt.imshow(img)
plt.show()