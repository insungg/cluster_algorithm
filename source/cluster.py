import random
import itertools
import pickle
import copy
from distance import measure
def cluster(N_iter, N_small, step=100, saturation=0, N_big=16, size_box=7, size_big=1, size_small=0.05):
    # initialize configuration
    N_total = N_big + N_small
    positions = []
    big_centers = [0.5, 2.5, 4.5, 6.5]
    for x, y in itertools.product(big_centers, big_centers):
        positions.append([x, y])
    small_counter = 0
    small_starts = [1, 3, 5, 2, 4, 6]
    for i, j, x, y in itertools.product(small_starts, small_starts, range(20), range(20)):
        if small_counter >= N_small: break
        positions.append([i + size_small*x + size_small/2, j + size_small*y + size_small/2])
        small_counter += 1
    bunch = []
    bunch.append(copy.deepcopy(positions))
    # cluster algorithm
    for iter in range(1, N_iter+1):
        i = random.randint(0, N_total-1) 
        pocket = {i}
        rest = set(range(N_total))
        rest.remove(i)
        a = random.randint(0, 1) # choose reflection axis
        t = random.uniform(0, 7) # choose reflection parameter 
        pocket_iter = 0
        while pocket:
            i = random.choice(tuple(pocket))
            positions[i][a] = (2*t-positions[i][a]+7) % 7
            x1, y1  = positions[i]
            size_1 = size_big if i < N_big else size_small
            rest_original = list(rest)
            for j in rest_original:
                x2, y2  = positions[j]
                size_2 = size_big if j < N_big else size_small
                dx = measure((x1, 0), (x2, 0))
                dy = measure((0, y1), (0, y2))
                # check complete overlapping
                if size_1 > size_2 and dx <= (size_1-size_2)/2 and dy <= (size_1-size_2)/2:
                    positions[j][a] = (2*t-positions[j][a]+7) %7
                # check overlapping
                elif dx < (size_1+size_2)/2 and dy < (size_1+size_2)/2:
                    rest.remove(j)
                    pocket.add(j)
            pocket.remove(i)
            pocket_iter += 1
        if iter%step == 0 and iter >= saturation:
            bunch.append(copy.deepcopy(positions))
            print(f'Saved {iter}-th configuration, pocket_iter={pocket_iter}')
    # save configurations
    with open(f'Nsmall={N_small}_Nstep={step}.dat', 'wb') as f:
        pickle.dump(bunch, f)
