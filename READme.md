
# average-util 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)

A proposal and implementation for a lightweight, zero-import `average()` built-in function for the Python language.

## 💡 The Motivation
Python provides several global built-in functions for basic mathematics, such as `sum()`, `min()`, `max()`, and `len()`. However, calculating a simple arithmetic mean currently requires an import:
```python
import statistics
data = [10, 20, 30]
result = statistics.mean(data)
