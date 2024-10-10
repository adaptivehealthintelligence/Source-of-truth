# Source of truth

Status: Initial exploration.

## Development

Looking at the container neo4j to explore neo4j.

### TODO

- [ ] Explore Neo4j
- [ ] Data ingestion from a data source
- [ ] Data query from UI
- [ ] Data repoert from prepared query
- [ ] Integration with Django

### Local Development

to avoid conflictys the follwing chnages have been made:
discovery: 5000 → 5001
cluster.raft: 7000 → 7001

## Loading Data

Add a node via:

> CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
> CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
> CREATE (Carrie:Person {name:'Carrie-Anne Moss', born:1967})

Add edges via:

> CREATE
> (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
> (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrix),
> (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrix),
> (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrix),
> (AndyW)-[:DIRECTED]->(TheMatrix),
> (LanaW)-[:DIRECTED]->(TheMatrix),
> (JoelS)-[:PRODUCED]->(TheMatrix)

This assumes in the same file, what happens if not in the same file???
You need to get the linked nodes if you don't have them eg (note the create can have multi creations):

> MATCH (Keanu:Person) WHERE Keanu.name = 'Keanu Reeves'
> CREATE

    (TheMatrixReloaded:Movie {title:'The Matrix Reloaded', released:2003, tagline:'Free your mind'}),
    (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixReloaded),

Note you can match by ID:

> MATCH (prsn:Person) WHERE ID(prsn) = Keanu

## Decisions

Store nodes in specific files.
Define a std id for each.
Links must be via these ids or a defined set.
