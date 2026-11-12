"""Command-line entry point."""

import argparse

import numpy as np

from .core import count_cells


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Count cells in a 2D image stored as .npy")
    parser.add_argument("image")
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--min-area", type=int, default=1)
    args = parser.parse_args(argv)
    stats = count_cells(np.load(args.image), args.threshold, args.min_area)
    print(f"cells: {stats.count}  mean area: {stats.mean_area:.1f} px")
