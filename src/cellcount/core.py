"""Threshold, label and measure cells."""

from dataclasses import dataclass

import numpy as np
from scipy import ndimage


@dataclass
class CellStats:
    """Summary of the cells found in one image."""

    count: int
    areas: np.ndarray

    @property
    def mean_area(self) -> float:
        return float(self.areas.mean()) if self.count else 0.0


def threshold_image(image: np.ndarray, threshold: float) -> np.ndarray:
    """Return a boolean mask of the pixels brighter than ``threshold``."""
    if image.ndim != 2:
        raise ValueError("expected a 2D image")
    return image > threshold


def count_cells(image: np.ndarray, threshold: float = 0.5, min_area: int = 1) -> CellStats:
    """Count the connected bright regions of at least ``min_area`` pixels."""
    labels, n = ndimage.label(threshold_image(image, threshold))
    if n == 0:
        return CellStats(0, np.array([], dtype=int))
    areas = np.bincount(labels.ravel())[1:]
    areas = areas[areas >= min_area]
    return CellStats(int(areas.size), areas)
