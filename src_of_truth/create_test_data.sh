#/bin/zsh

# use $@ to retain spaces in arguments
# poetry run python main.py "$@"

# run using a local docker instance
# poetry run python main.py http://127.0.0.1:7687 neo4j Blah1234!

read -p "This will destroy your current data, are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

poetry run python main.py exe_file_query cypher/delete_all.cypher
poetry run python main.py exe_file_query cypher/create_small.cypher
