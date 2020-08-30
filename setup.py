from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="helloworld-mkmenta",
    version="0.0.1",
    description="Say hello!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkmenta/python-package-example",
    author="Mikel Menta Garde",
    author_email="thisisnotmyemail@gmail.com",
    py_modules=["helloworld"],
    package_dir={"": "src"},
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
