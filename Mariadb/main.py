import mysql.connector

conn = mysql.connector.connect(

    host="localhost",
    user="root",
    password="adm123",
    database="maria"

)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cargo VARCHAR(255)
)
"""
cursor.execute(create_table_query)
conn.commit()

insr = "INSERT INTO funcionarios (nome, cargo) VALUES (%s, %s)"
dt = ("Ismael", "Developer")
cursor.execute(insr, dt)
conn.commit()

consulta_query = "SELECT * FROM funcionarios"
cursor.execute(consulta_query)


for (x, nome, cargo) in cursor:
    print(f"ID: {x}, Nome: {nome}, Cargo: {cargo}")

atualizar_dados = "UPDATE funcionarios SET cargo = %s WHERE nome = %s"
cargoN = ("Gerente", "Ismael")
cursor.execute(atualizar_dados, cargoN)
conn.commit()

delete = "DELETE FROM funcionarios WHERE id = %s AND nome = %s"
idtodel = (13, "Ismael")
idtodel = tuple(idtodel)

cursor.execute(delete, idtodel)
conn.commit()

cursor.close()
conn.close()
