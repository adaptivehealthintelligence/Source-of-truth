#/bin/zsh

# use $@ to retain spaces in arguments
# poetry run python main.py "$@"

# to access browser use http://127.0.0.1:7474/browser/

# this is the conmtainer version
# docker run \
    # --publish=7474:7474 --publish=7687:7687 \
    # --volume=./container_data:/data \
    # -d neo4j

# this is the local version
export NEO4J_HOME="/Users/tcoo5239/Library/Application Support/Neo4j Desktop/Application/relate-data/dbmss/dbms-7e2ec58e-7220-4352-9df2-c55e056a8288"
export NEO4J_IMPORT="$NEO4J_HOME/import"

echo starting neo4j...
"$NEO4J_HOME/bin/neo4j" start
