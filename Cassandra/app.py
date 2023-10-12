from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('mytest')

crtTable_query = """
CREATE TABLE IF NOT EXISTS mytable (
    id UUID PRIMARY KEY,
    nome text,
    idade int
);
"""

insertDt_query = """
INSERT INTO mytest.mytable (id, nome, idade)
VALUES (uuid(), 'Ismael', 16);
"""

nome = 'Ismael'
idade = 16


session.execute(crtTable_query)
session.execute(insertDt_query)

slct_query = "SELECT * FROM mytable;"
result = session.execute(slct_query)

for row in result:
    print(row)
