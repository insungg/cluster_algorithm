import os
import glob
import matplotlib.pyplot as plt
from drawBox import draw_configuration
from distance import average_nearest_distance
def read_positions(filename):
    positions = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().strip('[]')  # remove [] 
            x, y = map(float, line.split(','))  # get x, y seperated by comma
            positions.append((x, y)) 
    return positions
def extract_N_iter(filename):
    string = filename.split('_')[1]  # split by '_' and get the second part of "N_iter=300"
    value = string.split('=')[1]  # split by '=' and take the second part
    return int(value) 
# directory = 'backup'
directory = ''
N_small = 3000
# get a list of all files and sort by N_iter 
file_pattern = os.path.join(directory, f'N_iter=*_N_small={N_small}.txt')
files = glob.glob(file_pattern)
files = sorted(files, key=extract_N_iter)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.2, 10), gridspec_kw={'height_ratios': [10, 2]})
nearest = []
step = extract_N_iter(files[1])-extract_N_iter(files[0])
N_iter = extract_N_iter(files[-1])
for i, filename in enumerate(files):
    positions = read_positions(filename)  
    nearest.append(average_nearest_distance(positions[:16]) - 1) # min distance = 1 
    ax1.clear()
    ax2.clear()
    draw_configuration(ax1, positions)
    ax1.set_title(filename.split('.')[0])
    ax2.plot(nearest)
    ax2.set_title('Average Nearest Distance of Big Boxes')
    ax2.set_xlabel(f'N_iter/{step}')
    ax2.set_ylabel(r'Distance $-$ 1')
    plt.draw()
    plt.pause(0.5)
    # fig.savefig(f'output_config_{i}.png')
plt.show()
fig.savefig(f'final_configuration_N_small={N_small}_N_iter={N_iter}.pdf', pdf)
