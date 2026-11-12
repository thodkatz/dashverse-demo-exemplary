# cellcount

[![Tests](https://github.com/thodkatz/dashverse-demo-exemplary/actions/workflows/tests.yml/badge.svg)](https://github.com/thodkatz/dashverse-demo-exemplary/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8F%20%20%E2%97%8B-orange)](https://fair-software.eu)

Count and measure cells in 2D microscopy images with a simple threshold-and-label pipeline.

This repository is a **demo** for the EVERSE DashVERSE dashboards: it plays the part of a well-maintained research
software package, and its quality is assessed by `resqui` on every push.

## Installation

```sh
pip install .
```

Or with Docker:

```sh
docker build -t cellcount .
docker run --rm -v "$PWD:/data" cellcount /data/image.npy
```

## Usage

```python
import numpy as np
from cellcount import count_cells

image = np.load("image.npy")
result = count_cells(image, threshold=0.5)
print(result.count, result.mean_area)
```

From the command line:

```sh
cellcount image.npy --threshold 0.5
```

## Tests

```sh
pip install -e .[test]
pytest
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report bugs and ask questions in the
[issue tracker](https://github.com/thodkatz/dashverse-demo-exemplary/issues).

## Citation

If you use cellcount, please cite it as described in [CITATION.cff](CITATION.cff).

## License

MIT, see [LICENSE](LICENSE).
