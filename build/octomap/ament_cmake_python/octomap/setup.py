from setuptools import find_packages
from setuptools import setup

setup(
    name='octomap',
    version='2.1.5',
    packages=find_packages(
        include=('octomap', 'octomap.*')),
)
