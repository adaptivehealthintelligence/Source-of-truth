# list all nodes
MATCH (n) RETURN distinct labels(n)

# 
(mark), 

and mark.name = "Mark Jones" 
(mark)-[:WORKED_ON {roles:['Lead Statician']}]->(motc),
(mark)-[:WORKED_ON {roles:['Lead Statician']}]->(mfit)
