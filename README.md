# Fuzzy C-means
Python Implementation of Fuzzy C-means clustering algorithm


The Fuzzy C-means (FCM) algorithm is a clustering technique that allows data points to belong to multiple clusters with varying degrees of membership. It is an extension of the traditional k-means clustering algorithm, which assigns each data point to a single cluster.

The FCM algorithm works by minimizing an objective function that measures the quality of clustering. The algorithm involves the following steps:

1. Initialize the fuzzy partition matrix randomly, where each element represents the degree of membership of a data point to a cluster.
2. Calculate the cluster centroids based on the current fuzzy partition matrix.
3. Update the fuzzy partition matrix based on the new cluster centroids and a fuzziness parameter (m), which controls the degree of fuzziness of the clustering.
4. Repeat steps 2 and 3 until the changes in the fuzzy partition matrix are below a predefined threshold or a maximum number of iterations have been reached.

The fuzziness parameter (m) affects the degree to which data points can belong to multiple clusters. When m is close to 1, the FCM algorithm behaves more like the traditional k-means algorithm, whereas when m is larger, the algorithm allows for a higher degree of fuzziness in the clustering.

The FCM algorithm is particularly useful in situations where the boundaries between clusters are not well-defined, and data points can naturally belong to multiple clusters. Applications of FCM can be found in various domains, including image processing, pattern recognition, and data mining.

The main script is available at `FuzzyCMean.py`
