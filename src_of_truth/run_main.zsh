#/bin/zsh

# use $@ to retain spaces in arguments
# poetry run python main.py "$@"

# run using a local docker instance
# poetry run python main.py http://127.0.0.1:7687 neo4j Blah1234!

poetry run python main.py "$@"
