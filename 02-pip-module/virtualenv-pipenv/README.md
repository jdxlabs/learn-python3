# Pipenv Setup

```bash
# Install pipenv first
brew install pipenv
```

```bash
# Create the Pipfile
pipenv install

# You can install packages, or edit Pipfile directly
pipenv install requests
pipenv install numpy


# Activate/Deactivate the venv
pipenv shell  # and Ctrl + D to quit

# Alternatively, run a command inside the virtualenv
pipenv run python

# Uninstall the venv
pipenv --rm
```
