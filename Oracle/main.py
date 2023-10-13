import cx_Oracle

conn = cx_Oracle.connect("ismael/@//localhost:1521/XBPDB1")
cursor = conn.cursor()
