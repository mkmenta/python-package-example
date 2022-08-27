from setuptools import setup
from helloworld import __version__, __url__, __author__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="helloworld-mkmenta",
    version=__version__,
    description="Say hello!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    author_email="thisisnotmyemail@gmail.com",
    packages=["helloworld"],
    # You can take classifiers from https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "termcolor >= 1.1.0"  # we don't really need this to be >=1.1.0, is just to give an example
    ],
    extras_require={
        "dev": [
            "pytest",
            "pydocstyle",
            "pycodestyle"
        ]
    }
)
