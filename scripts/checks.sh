# exit if any command fails
set -e

# printf "Formatting Check\n"
# black src --check

# printf "\nTyping Check\n"
# mypy src

printf "\nLint Check\n"
pylint src
