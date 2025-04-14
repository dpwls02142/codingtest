import sys
n = int(sys.stdin.readline().rstrip())
vectors, lines = [], []
for _ in range (6):
    vector, line = map(int, sys.stdin.readline().rstrip().split())
    vectors.append(vector)
    lines.append(line)
max_width_idx, max_height_idx = -1, -1
max_width, max_height = 0, 0
for i in range(6):
    if vectors[i] == 1 or vectors[i] == 2:
        if lines[i] > max_width:
            max_width = lines[i]
            max_width_idx = i
    else:
        if lines[i] > max_height:
            max_height = lines[i]
            max_height_idx = i
small_width_idx = (max_height_idx + 3) % 6
small_height_idx = (max_width_idx + 3) % 6
small_width = lines[small_width_idx]
small_height = lines[small_height_idx]
print(((max_width * max_height) - (small_width * small_height)) * n)