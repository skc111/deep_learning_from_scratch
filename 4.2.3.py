import numpy as np
from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
   load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape) 
print(t_train.shape) 

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
