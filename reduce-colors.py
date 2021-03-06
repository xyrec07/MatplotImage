import numpy as np
from skimage import io
from sklearn.cluster import KMeans

original = io.imread('path to image') # path to image
n_colors = 20 # Number of colors in final image 

arr = original.reshape((-1, 3))
kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(arr)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
less_colors = centers[labels].reshape(original.shape).astype('uint8')

io.imsave('output path',less_colors)
