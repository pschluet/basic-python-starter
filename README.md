# basic-python-starter
python starter repo with a CI pipeline that runs CI checks

## Setup
```
brew update
brew install pyenv
pyenv install 3.11.4
python -m venv .venv
source .venv/bin/activate
pip install -r dev-requirements.txt
```

## Scripts
1. `scripts/checks.sh`: performs the same static code checks that the CI/CD pipeline runs
1. `scripts/format.sh`: auto-formats the code using Black
1. `scripts/test.sh`: runs unit tests