import sklearn
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

blob_centres = np.array([[1.2 , 3.5] , [-1.2, 3.2], [-2.4, 5.2], [4.1, -2.6]])

blob_std = [0.4 , 0.3 , 0.1 , 0.1 , 0.5 , 0.2]

X, y = make_blobs(n_samples = 2000 , centers = blob_centres, cluster_std = blob_std, random_state = 7)

plt.figure(figsize = (8, 4))
plot_clusters(X)
plt.show()