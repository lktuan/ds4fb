from setuptools import find_packages, setup

setup(
    name="ds4fb",
    version="0.1.0",
    packages=find_packages(where="notebooks"),
    package_dir={"": "notebooks"},
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.2.0",
        "numpy>=1.26.0",
        "scikit-learn>=1.4.0",
        "scipy>=1.12.0",
        "statsmodels>=0.14.1",
        "torch>=2.2.0",
        "tensorflow>=2.15.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
            "black>=24.1.0",
            "isort>=5.13.0",
            "flake8>=7.0.0",
            "pytest>=8.0.0",
            "pre-commit>=3.6.0",
        ],
    },
)
