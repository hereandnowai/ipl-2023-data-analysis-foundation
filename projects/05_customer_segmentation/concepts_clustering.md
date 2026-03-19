# Section 6: PROJECT-SPECIFIC CONCEPTS - K-Means Intuition

In clustering, we don't have a target label like "Price" or "Survived". We just have data, and we want to find **natural groups**.

### The Math: Euclidean Distance
We calculate how close points are to **centroids** (the center point of a cluster).

$$d = \sqrt{\sum (x_i - y_i)^2}$$

### The Algorithm (Simplified)
1. Initialize $K$ random centroids.
2. Assign each point to the closest centroid.
3. Move centroids to the average position of their points.
4. Repeat until stable.
