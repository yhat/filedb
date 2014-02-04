from distutils.core import setup
from setuptools import find_packages

setup(
    name='filedb',
    version='0.2.3',
    author="Greg Lamp",
    author_email="greg@yhathq.com",
    url="https://github.com/yhat/filedb",
    packages=find_packages(),
    description="Create a file that pretends to be a database query",
    license='BSD',
    long_description=open('README.rst').read(),
    scripts=['bin/filedb'],
    install_requires=[
        "docopt==0.6.1",
        "fusepy==2.0.2",
        "pymongo==2.6.3"
    ]
)
