
Virtual envionments allow you to have distinct versions of packages for your different projects.


There are different ways to create virtual environments:

- Using [Venv](https://docs.python.org/3/library/venv.html), the built-in module for creating virtual environments in Python 3.
- Using [Virtualenv](https://virtualenv.pypa.io/en/stable), a third-party tool that provides similar functionality as venv but works with both Python 2 and Python 3.
- Using [Conda](https://conda.io/docs), a package and environment management system often used in data science and scientific computing.
- Using [Pipenv](https://pipenv.pypa.io/en/stable), a higher-level tool that combines package management and virtual environment management, using Pipfile.

If you use Pyenv, you can also use [Pyenv-Virtualenv](https://github.com/pyenv/pyenv-virtualenv) to create a virtual environment, that allows to switch between different venvs direclty coupled with Pyenv.
This plugin isn't necessary, you can use the other libraries, even if you use Pyenv.


You will find some examples in the next section "02-pip-module", for Venv, Pipenv and Pyenv-Virtualenv.
