import matplotlib.pyplot as plt
import matplotlib.patches as patches
def draw_box(ax, x, y, size, size_big=1, siez_box=7):
    lower_left_corner = (x - size/2, y - size/2)
    rect = []
    if size == size_big:
        rect = patches.Rectangle(lower_left_corner, size, size, edgecolor='blue', facecolor='blue', linewidth=1)
    else:
        rect = patches.Rectangle(lower_left_corner, size, size, color='gray')
    ax.add_patch(rect)
def draw_configuration(ax, positions, size_small=0.05, size_big=1, siez_box=7, N_big=16):
    ax.clear()
    ax.set_xlim(0, siez_box)
    ax.set_ylim(0, siez_box)
    for idx, (x, y) in enumerate(positions):
        size = size_big if idx < N_big else size_small
        draw_box(ax, x, y, size, siez_box)
        if x - size / 2 < 0:  # left boundary
            draw_box(ax, x + siez_box, y, size, siez_box)
        if x + size / 2 > siez_box:  # right boundary
            draw_box(ax, x - siez_box, y, size, siez_box)
        if y - size / 2 < 0:  # bottom boundary
            draw_box(ax, x, y + siez_box, size, siez_box)
        if y + size / 2 > siez_box:  # top boundary
            draw_box(ax, x, y - siez_box, size, siez_box)
        # handle corner cases
        if (x - size / 2 < 0 and y - size / 2 < 0):  # bottom-left corner
            draw_box(ax, x + siez_box, y + siez_box, size, siez_box)
        if (x + size / 2 > siez_box and y - size / 2 < 0):  # bottom-right corner
            draw_box(ax, x - siez_box, y + siez_box, size, siez_box)
        if (x - size / 2 < 0 and y + size / 2 > siez_box):  # top-left corner
            draw_box(ax, x + siez_box, y - siez_box, size, siez_box)
        if (x + size / 2 > siez_box and y + size / 2 > siez_box):  # top-right corner
            draw_box(ax, x - siez_box, y - siez_box, size, siez_box)
