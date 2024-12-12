def measure(position1, position2, size_box = 7):
    x1, y1 = position1
    x2, y2 = position2
    dx = min(size_box-abs(x1-x2), abs(x1-x2))
    dy = min(size_box-abs(y1-y2), abs(y1-y2))
    return (dx**2 + dy**2)**0.5
def mean(a):
    return sum(a)/len(a)
def nearest_distance(positions, N_big = 16, size_box = 7):
    distances = []
    for i in range(N_big):
        nearest = size_box*2
        for j in range(N_big):
            if i == j: continue
            candidate = measure(positions[i], positions[j])
            if candidate < nearest:
                nearest = candidate
        distances.append(nearest)
    return distances
def average_nearest_distance(positions, N_big = 16, size_box = 7):
    return mean(nearest_distance(positions, N_big, size_box))
def average_distance(positions, N_big = 16, size_box = 7):
    distances = []
    for i in range(N_big):
        for j in range(i+1, N_big):
            distances.append(measure(positions[i], positions[j]))
    return mean(distances)
