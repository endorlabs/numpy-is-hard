import numpy as np

required_version = "1.25.3"
installed_version = np.__version__

if installed_version != required_version:
    raise RuntimeError(
        f"Incorrect NumPy version: {installed_version}. "
        f"Please install NumPy {required_version} by running:\n"
        f"pip install numpy=={required_version}"
    )

print(f"NumPy version {installed_version} is correctly installed.")
