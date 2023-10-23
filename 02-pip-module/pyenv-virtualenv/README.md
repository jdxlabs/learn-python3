# Pyenv-Virtualenv Setup

```bash
# Install pyenv-virtualenv first
brew install pyenv-virtualenv

# You can list the venvs
pyenv virtualenvs
```

```bash
# Create the venv
pyenv virtualenv demo-app

# Activate/Deactivate the venv
pyenv activate demo-app
pyenv deactivate

# Alternatively, you can initiate a shell
pyenv shell demo-app
# and unset the shell
pyenv shell --unset
# Be carreful, if you are in the "Shell" context, you are not in the "Global" context
# You have to unset the shell if you want to use the "pyenv global <my-version>" command

# Here is a command to know if you are in the Shell context or not (because there is no indicator on the prompt)
pyenv version
# or check the env var
echo $PYENV_VERSION

# Once you are in the shell context (or activated the venv), Install the requirements
pip install -r requirements.txt

# Remove the venv
pyenv uninstall demo-app
```
