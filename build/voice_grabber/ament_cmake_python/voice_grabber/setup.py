from setuptools import find_packages
from setuptools import setup

setup(
    name='voice_grabber',
    version='0.0.0',
    packages=find_packages(
        include=('voice_grabber', 'voice_grabber.*')),
)
