from setuptools import setup, find_packages
import os

path = os.path.join(os.path.abspath("."), "README.md")

if os.path.exists(path):
    with open(path, "r") as f:
        long_description = f.read()
else:
    long_description = ""

setup(
    name="fs_mng_app",
    version="1.0.0",
    description="File System Management App",
    long_description=long_description,
    packages=find_packages()
)