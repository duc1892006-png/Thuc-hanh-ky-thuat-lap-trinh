import numpy as np

student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0]

# Sort by height, then id
sorted_indices = np.lexsort((student_id, student_height))

print("Sorted indices:", sorted_indices)
print("Sorted data:")
for idx in sorted_indices:
    print(student_id[idx], student_height[idx])
