import numpy as np
import pytest

from cellcount import count_cells, threshold_image


def two_cells():
    image = np.zeros((10, 10))
    image[1:3, 1:3] = 1.0
    image[6:9, 6:9] = 1.0
    return image


def test_counts_separate_regions():
    stats = count_cells(two_cells())
    assert stats.count == 2
    assert sorted(stats.areas) == [4, 9]


def test_min_area_drops_small_regions():
    assert count_cells(two_cells(), min_area=5).count == 1


def test_empty_image():
    stats = count_cells(np.zeros((4, 4)))
    assert stats.count == 0
    assert stats.mean_area == 0.0


def test_rejects_3d():
    with pytest.raises(ValueError):
        threshold_image(np.zeros((2, 2, 2)), 0.5)
