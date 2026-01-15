from setuptools import setup, find_packages

setup(
    name="qiskit_peres_gate",  # The name people will use for 'pip install'
    version="0.1.0",
    author="Arnab Dinda",
    author_email="arnabexpress3.12@gmail.com",
    description="A library to add the Peres Gate (New Toffoli Gate) functionality to Qiskit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arnabdevv/peres_gate_project.git",
    packages=find_packages(),
    install_requires=[
        "qiskit>=1.0.0",  # Ensures the user has a modern version of Qiskit
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
)
