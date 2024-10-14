#/bin/bash

# load the data fro man excel file into the neo4j database
# destroying tyhe original contents of the database

# run using a local docker instance
# poetry run python main.py http://127.0.0.1:7687 neo4j Blah1234!

poetry run python main.py del_all

poetry run python main.py load_excel "../data/Sample-data.xlsx"

poetry run python main.py get_all

