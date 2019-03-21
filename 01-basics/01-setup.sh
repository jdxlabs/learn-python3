#!/usr/bin/env bash

if [[ "$(uname)" == "Darwin" ]]; then
    # for mac users (.. assuming you are using Brew)
    # if not, just install it before : https://brew.sh/
    brew install python3
else
    # for linux users (.. assuming you are using Debian)
    # for other distributions, just do the same with the appropriate package manager
    sudo apt install python3
fi

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# for windows users, there are also packages for you :
# https://www.python.org/downloads/windows/
