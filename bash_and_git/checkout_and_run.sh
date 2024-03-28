#! /bin/bash

set -euxo pipefail

rm -rf fudge

# This script clones out a git repository and runs a python script from it.

# The git repository to check out:
GIT_REPO="https://github.com/clusterfudgeai/fudge.git"
GIT_BRANCH="main"

# The path to the python script to run:
PYTHON_SCRIPT="python/clusterfudge_examples/bash_and_git/hello_world.py"

# The directory to clone the git repository into:
CLONE_DIR="fudge"

# Clone the git repository:
git clone "$GIT_REPO" "$CLONE_DIR"

# Check out the specified branch:
cd "$CLONE_DIR"
git checkout "$GIT_BRANCH"

# Run the python script from the git repository:
python3 "$PYTHON_SCRIPT"
