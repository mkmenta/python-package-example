# Python Package Example
![Formatting and tests workflow](https://github.com/mkmenta/python-package-example/actions/workflows/main-action.yml/badge.svg)

This repository contains a basic python package example with the aim of showing how a good python package should look like.

Install:
```
pip install helloworld-mkmenta
```
Install locally:
```
git clone https://github.com/mkmenta/python-package-example.git
cd python-package-example
pip install -e .
```

### Usage
You will find an usage example [here](examples/say_hello_example.py).

## Documentation
This project has a documentation in *readthedocs.io* generated using `sphinx`: [documentation](https://python-package-example.readthedocs.io/en/latest/index.html).

Find the tutorial on how it was created [here](https://python-package-example.readthedocs.io/en/latest/tutorials/documentation.html).

## Developing
To install the package along with the tools you need to develop it run the following (local installation with the `"dev"` extras:
```
git clone https://github.com/mkmenta/python-package-example.git
cd python-package-example
pip install -e ."[dev]"
```
If you are developing, you should run `pip install -e .` every time you change `setup.py` or the dependencies etc. to make sure that everything works.

### A note about requirements
The requirements needed to **run** the package should go in the `install_requires` argument of `setup()` in the `setup.py`.

The requirements needed to **develop** the package should go in the `extras_require` argument dict (under the `"dev"` key) of `setup()` in the `setup.py`.

This is preferred to a `requirements.txt` file, because this is code and it can be understood directly during the installation of the package itself.

The `requirements.txt` should be used to recreate enviroments with specific versions (e.g.`requests==2.22.0`), not to share software.

### Building and distribution
Build without install i.e. build wheel:
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

### Code format checks and tests (GitHub Actions for continuous integration)
In order to check the code format and test it, this project runs a GitHub action defined in [`.github/workflows/main-action.yml`](.github/workflows/main-action.yml).

You can check the execution of this action [here](https://github.com/mkmenta/python-package-example/actions/workflows/main-action.yml).

This allows blocking any merge of a pull request if the code is not correcly formatted or tests are not passing. In order to do that you can go to `Settings -> Branches -> Add rule`

### Other useful stuff
- This repo is prepared for PyCharm and it has some run configurations (in `.idea/runConfigurations`).

## References
- Mark Smith - Publish a (Perfect) Python Package on PyPI ([video](https://www.youtube.com/watch?v=GIF3LaRqgXo))
- `.gitignore` file from https://gitignore.io/
- License from https://choosealicense.com/
- PyPI classifiers from https://pypi.org/classifiers/
- Autodocumenting your Python code with Sphinx(
[part1](https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-i-5/)
[part2](https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/))
)
- A Simple Tutorial on How to document your Python Project using Sphinx and Rinohtype (
[post](https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b)
)