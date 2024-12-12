from cluster import cluster
import pickle
import multiprocessing as mp
def run_cluster(i):
    return cluster(10000, i, 50)
if __name__ == "__main__":
    # i_values = range(200, 5100, 100)
    i_values = [3350, 3450, 3550, 3650, 3750, 3850, 3950, 4050, 5200, 5300, 5400, 5500]
    num_cores = 8
    with mp.Pool(processes=num_cores) as pool:
        results = pool.map(run_cluster, i_values)
# with open("Nsmall=190_Nstep=50.dat", 'rb') as f:
#     positions = pickle.load(f)
# print(len(positions))
# print(len(positions[1]))
# print(len(positions[1][1]))
