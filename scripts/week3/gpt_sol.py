# -----------------------------
# 1. Import libraries
# -----------------------------
import matplotlib
matplotlib.use("TkAgg")


from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# -----------------------------
# 2. Load Wine dataset
# -----------------------------
wine = datasets.load_wine()

X = wine.data
y = wine.target

print("Original data shape:", X.shape)
print("Feature names:", wine.feature_names)


# -----------------------------
# 3. PCA with 2 components
# -----------------------------
pca = PCA(n_components=2)

# Fit PCA and transform the original 13 features into 2 PCs
X_pca = pca.fit_transform(X)

print("\nPCA shape:", X_pca.shape)

print("Explained variance ratio:")
print(pca.explained_variance_ratio_)

print("Total explained variance:")
print(pca.explained_variance_ratio_.sum())


# -----------------------------
# 4. K-Means clustering
# -----------------------------
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train K-Means on the PCA data
clusters = kmeans.fit_predict(X_pca)

print("\nCluster assignments:")
print(clusters)


# -----------------------------
# 5. Get cluster centers
# -----------------------------
centers = kmeans.cluster_centers_

print("\nCluster centers:")
print(centers)


# -----------------------------
# 6. Plot PCA data + KMeans clusters
# -----------------------------
plt.figure(figsize=(8, 6))

# Plot the wines using PC1 and PC2
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters
)

# Plot the 3 cluster centers
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Wine PCA with K-Means Clustering")

plt.show()

# -----------------------------
# 7. Compare KMeans with actual Wine classes
# -----------------------------
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics.cluster import contingency_matrix

print("\nActual wine classes:")
print(y)

print("\nKMeans clusters:")
print(clusters)


# Compare actual classes with discovered clusters
ari = adjusted_rand_score(y, clusters)

print("\nAdjusted Rand Index:")
print(ari)


# Show how actual classes correspond to KMeans clusters
comparison = contingency_matrix(y, clusters)

print("\nActual classes vs KMeans clusters:")
print(comparison)


# -----------------------------
# 8. Plot actual Wine classes
# -----------------------------
plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Actual Wine Classes")

plt.show()


# -----------------------------
# 9. Plot KMeans clusters
# -----------------------------
plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters
)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - KMeans Clusters")

plt.show()