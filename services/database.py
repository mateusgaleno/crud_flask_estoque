
from mysql.connector  import (connection)
db_connection = connection.MySQLConnection(host='database-1.ctwwml9iw6rq.sa-east-1.rds.amazonaws.com',
user='admin', password='Dfiquer1', database='projeto_trader')
cursor = db_connection.cursor()

