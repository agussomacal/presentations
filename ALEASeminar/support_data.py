from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter
from tqdm import tqdm

from ALEASeminar.config import *
from ALEASeminar.config import material_dir


def save_fig_without_white(filename):
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()


axes_xy_proportions = (4, 4)
number_of_measures = 1000
path_subcell = Path(material_dir, "SubCell")
solution = np.array(plt.imread(f"{path_subcell}/solution.png").tolist())[:, :, 0]
solution = solution / np.max(solution)
lx, ly = np.shape(solution)
np.random.seed(0)
points = np.array([(np.random.choice(lx), np.random.choice(ly)) for _ in range(number_of_measures)], dtype=int)
fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
alpha = 0
ax.imshow(solution, origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1, alpha=alpha)
ax.scatter((-points[:, 1] + lx / 2) / lx * 2, (points[:, 0] - ly / 2) / ly * 2,
           c=[solution[p[1], p[0]] for p in points],
           s=30, cmap="viridis", vmin=-1, vmax=1,  # linewidths=2, edgecolors="black"
           )
save_fig_without_white(f"{path_subcell}/solution_pointwise.png")

# -------- yoda ---------- #
yoda = np.array(plt.imread(f"{images_dir}/yoda.jpg").tolist())[:, :, 0]
fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
ax.imshow(yoda / np.max(yoda), origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1)
save_fig_without_white(f"{path_subcell}/yoda.png")


# -------- yodas pointwise ---------- #
def plot_pointwise(ax, img, indexes, alpha=0):
    ax.imshow(img, origin='upper', cmap="viridis", extent=(0, 1, 0, 1), vmin=-1, vmax=1, alpha=alpha)
    ax.scatter(indexes[:, 0] / lx, 1 - indexes[:, 1] / ly,
               c=[img.T[p[0], p[1]] for p in indexes],
               s=30, cmap="viridis", vmin=-1, vmax=1,
               # linewidths=2, edgecolors="black"
               )


yoda = yoda / np.max(yoda)
lx, ly = np.shape(yoda)
np.random.seed(0)
indexes = np.random.choice(np.min((lx, ly)), size=(number_of_measures, 2))

fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
plot_pointwise(ax, yoda, indexes)
save_fig_without_white(f"{path_subcell}/yoda_pointwise.png")


# -------- yoda avgs ---------- #
def calculate_averages_from_image(image, num_cells_per_dim):
    # Example of how to calculate the averages in a single pass:
    # np.arange(6 * 10).reshape((6, 10)).reshape((2, 3, 5, 2)).mean(-1).mean(-2)
    img_x, img_y = np.shape(image)
    ncx, ncy = (num_cells_per_dim, num_cells_per_dim) if isinstance(num_cells_per_dim, int) else num_cells_per_dim
    return image.reshape((ncx, img_x // ncx, ncy, img_y // ncy)).mean(-1).mean(-2)


yoda_avg = calculate_averages_from_image(yoda, num_cells_per_dim=10)
fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
ax.imshow(yoda_avg / np.max(yoda_avg), origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1)
save_fig_without_white(f"{path_subcell}/yoda_avg10.png")

yoda_avg = calculate_averages_from_image(yoda, num_cells_per_dim=20)
fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
ax.imshow(yoda_avg / np.max(yoda_avg), origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1)
save_fig_without_white(f"{path_subcell}/yoda_avg20.png")


# -------- yodas approximations ---------- #
def approx_filter(img, n, sigma=7):
    img_avg = calculate_averages_from_image(img, num_cells_per_dim=n)
    resolution_factor = np.array(np.shape(img)) / n
    img_avg = np.repeat(np.repeat(img_avg, resolution_factor[0], axis=0), resolution_factor[1], axis=1)
    return gaussian_filter(img_avg, sigma=sigma)


subdivisions = [2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 24, 28]
min_n = 10
subdivisions = [min_n, 15, 20, 24, 28]
for i, n in enumerate(subdivisions):
    yoda_approx = approx_filter(img=yoda, n=n, sigma=lx / 2 / n) / np.max(yoda)

    fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
    ax.imshow(yoda_approx, origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1)
    save_fig_without_white(f"{path_subcell}/yoda_approx_{n}.png")

    fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
    ax.imshow(np.abs(yoda - yoda_approx) ** 2, origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1)
    save_fig_without_white(f"{path_subcell}/yoda_approx_diff_{n}.png")

    fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
    plot_pointwise(ax, yoda_approx, indexes)
    save_fig_without_white(f"{path_subcell}/yoda_approx_pointwise_{n}.png")

    fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
    plot_pointwise(ax, np.abs(yoda - yoda_approx) ** 2, indexes)
    save_fig_without_white(f"{path_subcell}/yoda_approx_diff_pointwise_{n}.png")

# fig, ax = plt.subplots(1, 1, figsize=axes_xy_proportions)
# ax.imshow(yoda_approx, origin='upper', cmap="viridis", extent=(-1, 1, -1, 1), vmin=-1, vmax=1)
# save_fig_without_white(f"{path_subcell}/yoda_rec.png")
