"""
Run `conda env create --file environment.yaml` to create an editable 
install of this project
"""

from setuptools import setup, find_packages

setup(
    name="Example Snowpark Python project",
    version="0.1.0",
    packages=find_packages()
)
