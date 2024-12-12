import sys
import matplotlib.pyplot as plt
from util import *
from draw import draw_configuration
from distance import average_nearest_distance
if len(sys.argv) <= 1:
    print("Usage: python3 drawEvolv.py (filename.dat)")
    sys.exit(1)
filename = sys.argv[1]
print(filename)
N_small, step = read_parameters(filename)
positions = read_positions(filename)  
nearest = []
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.2, 10), gridspec_kw={'height_ratios': [10, 2]})
for i in range(len(positions)):
    if i%4 == 1: continue
    nearest.append(average_nearest_distance(positions[i][:16]))
    ax1.clear()
    ax2.clear()
    draw_configuration(ax1, positions[i])
    ax1.set_title(rf'N_small = {N_small} @ Iteration={i*step}')
    ax2.plot(nearest)
    ax2.set_title('Average Nearest Distance of Big Boxes')
    ax2.set_xlabel(f'N_iter/{step}')
    ax2.set_ylabel(r'Distance')
    plt.draw()
    plt.pause(0.5)
    if i == len(positions)-1:
        plt.savefig(f'final_configuration_N_small={N_small}_N_iter={len(positions)*step}.pdf', pdf)
plt.show()
