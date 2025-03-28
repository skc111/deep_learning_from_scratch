from mnist import load_mnist
import numpy as np
from PIL import Image

def image_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
img = x_train[0]
lable = t_train[0]
print(lable)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

image_show(img)
