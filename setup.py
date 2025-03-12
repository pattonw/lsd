from Cython.Distutils import build_ext
from distutils.core import setup
from distutils.extension import Extension
from setuptools import find_packages

from pathlib import Path

this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()

setup(
        name='lsds',
        version='0.1.3',
        description='Local Shape Descriptors.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/funkey/lsd',
        author='Jan Funke',
        author_email='funkej@janelia.hhmi.org',
        license='MIT',
        packages=find_packages(),
        install_requires=[
            "numpy",
            "scipy",
            "h5py",
            "scikit-image",
            "requests",
            "gunpowder",
        ]
)
