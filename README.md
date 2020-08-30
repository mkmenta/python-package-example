# Python Package Example
This repository contains a basic python package example with the aim of showing how a good python package should look like.

Install:
```
pip install helloworld
```
Install locally:
```
git clone https://github.com/mkmenta/python-package-example.git
cd python-package-example
pip install -e .
```
If you are developing, you should run `pip install -e .` every time you change `setup.py` or the dependencies etc. to make sure that everything works.

Usage example:
```python
from helloworld import say_hello

# Generate "Hello world!"
say_hello()

# Generate "Hello mkmenta!"
say_hello("mkmenta")
```

### Developing
To install the package along with the tools you need to develop it run the following (local installation with the `"dev"` extras:
```
git clone https://github.com/mkmenta/python-package-example.git
cd python-package-example
pip install -e ."[dev]"
```
### A note about requirements
The requirements needed to **run** the package should go in the `install_requires` argument of `setup()` in the `setup.py`.

The requirements needed to **develop** the package should go in the `extras_require` argument dict (under the `"dev"` key) of `setup()` in the `setup.py`.

This is preferred to a `requirements.txt` file, because this is code and it can be understood directly during the installation of the package itself.

The `requirements.txt` should be used to recreate enviroments with specific versions (e.g.`requests==2.22.0`), not to share software.

### Building and distribution
Build without installi i.e. build wheel:
```
python3 setup.py bdist_wheel
```

Source distribution:
```
python3 setup.py sdist
```
For the source distribution, remember to:
- Check out the warnings of `python3 setup.py sdist`.
- Check that every file from the repo is packed in the tar file (`tar tzf dist/helloworld-X.X.X.tar.gz`) as written in the `MANIFEST.in`. A useful tool is `check-manifest`.

### Uploading to PyPI
```
python3 setup.py bdist_wheel sdist
twine upload dist/*
```

### Other useful stuff
- This repo is prepared for PyCharm and it has some run configurations (in `.idea/runConfigurations`).

## References
- Mark Smith - Publish a (Perfect) Python Package on PyPI ([video](https://www.youtube.com/watch?v=GIF3LaRqgXo&list=WL&index=9&t=779s))
- `.gitignore` file from [gitignore.io](gitignore.io)
- License from [choosealicense.com](choosealicense.com)
- PyPI classifiers from https://pypi.org/classifiers/
