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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    # TODO: it would be cool to show some install_requires usage
    extras_require={
        "dev": [
            "pytest>=3.7",
            "tox"
        ]
    }
)
