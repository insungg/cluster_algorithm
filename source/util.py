import os, glob
import pickle
import re
def read_parameters(filename):
    N_small_match = re.search(r"Nsmall=(\d+)", filename)
    step_match = re.search(r"Nstep=(\d+)", filename)
    N_small = int(N_small_match.group(1)) 
    step = int(step_match.group(1)) 
    return (N_small, step) 
def read_positions(filename):
    with open(filename, 'rb') as f:
        positions = pickle.load(f)
    return positions