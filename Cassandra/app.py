from cassandra.cluster import Cluster
import uuid

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('mytest')

crtTable_query = """
CREATE TABLE IF NOT EXISTS mytable (
    id UUID PRIMARY KEY,
    nome text,
    idade int
);
"""

session.execute(crtTable_query)


id = uuid.uuid4()
print(id)
nm = 'Ismael2'
age = '126'


insertDt_query = f"INSERT INTO mytest.mytable (id, nome, idade) VALUES (uuid(), '{nm}', {age})"
# session.execute(insertDt_query)




id = uuid.UUID('f4ed0526-f8d8-48cd-ab0a-10316928ec70')
upd_query = f"UPDATE mytable SET nome = 'pirolise99' WHERE id = {id};"  # --> del_query = f"DELETE FROM mytable WHERE id = {id};"

session.execute(upd_query)



slct_query = "SELECT * FROM mytable;"
result = session.execute(slct_query)

for row in result:
    print(row)
