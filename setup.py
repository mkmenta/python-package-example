import os
import sys
from importlib import import_module

from setuptools import setup

# If we do from helloworld import __version__ etc. we will get an error because requirements for imports in __init__.py
# are not yet installed. This is an ugly way to do it but I haven't found a better way.
sys.path.append(os.path.join(os.path.split(__file__)[0], "helloworld"))
info = import_module("_info")

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="helloworld-mkmenta",
    version=info.__version__,
    description="Say hello!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=info.__url__,
    author=info.__author__,
    author_email="thisisnotmyemail@gmail.com",
    packages=[
        "helloworld",
        "helloworld.utils"
    ],
    # You can take classifiers from https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "termcolor < 2.0.0"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pydocstyle",
            "pycodestyle"
        ]
    }
)
