MATCH (tom), (reena), (mark), (parveen), (motc)
WHERE 
    tom.name = "Tom Snelling" AND reena.name = "Reena D'Souza" 
    and mark.name = "Mark Jones" 
    and parveen.name = "Parveen Fathima" 
    and motc.title = "Motivate-C"
CREATE
(tom)-[:WORKED_ON {roles:['Cordinating Investigator']}]->(motc),
(mark)-[:WORKED_ON {roles:['Lead Statician']}]->(motc),
(parveen)-[:WORKED_ON {roles:['Advisor']}]->(motc),
(reena)-[:WORKED_ON {roles:['Trial Manager']}]->(motc);
