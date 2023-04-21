
from setuptools import find_packages
from setuptools import setup
import setuptools

from distutils.command.build import build as _build
import subprocess


REQUIRED_PACKAGES = [
    # Any additional packages beyond the base image 
    # would go here (not necessary for this tutorial) eg
    # 'transformers',
    # 'datasets'
    ]

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Vertex AI | Training | PyTorch | MNIST | Python Package'
)
