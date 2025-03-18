from setuptools import setup, find_packages

setup(
    name="simple_neuralnet",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "pillow",
    ],
    entry_points={
        'console_scripts': [
            'simple-neuralnet = simple_neuralnet:start_ui',  # Matches package name
        ],
    },
    author="Sai Mounik",
    description="A simple neural network library with UI for training and recognition",
    python_requires='>=3.9',  # Based on your Python version
)