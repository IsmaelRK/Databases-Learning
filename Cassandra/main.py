import uuid

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
INSERT INTO mytable (id, nome, idade)
VALUES (?, ?, ?)

"""

id = uuid.uuid4()
nome = 'Ismael'
idade = 16

session.execute(crtTable_query)
session.execute(insertDt_query, (id, nome, idade))
