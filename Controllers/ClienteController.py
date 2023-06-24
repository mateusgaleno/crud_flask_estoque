from ast import Return
import services.database as db;
import models.Cliente as cliente;

#função serve para incluir no banco de dados
def incluir(cliente):
        cursor = db.db_connection.cursor()
        comando_SQL = "INSERT INTO `projeto_trader`.`Cliente` (`cliNome`, `cliIdade`, `cliProfissao`) VALUES (%s,%s,%s)"
        dados = (str(cliente.nome), str(cliente.idade), str(cliente.profissao))
        cursor.execute(comando_SQL, dados)
        db.db_connection.commit()

def SelecionarById(id):
    db.cursor.execute("SELECT * FROM projeto_trader.Cliente  WHERE ID = {}".format(id))
    costmerList = []

    for row in db.cursor.fetchall(): # fetchal recupera todos os IDS selecionado acima
        costmerList.append(cliente.Cliente(row[0],row[1],row[2],row[3]))

    return costmerList[0]


def alterar(id):

    cursor = db.db_connection.cursor()
    sql_2 = "UPDATE projeto_trader.Cliente SET cliNome = %s, cliIdade =  %s, cliProfissao = %s WHERE id = str(cliente.id)"   
    val = (str(cliente.nome), str(cliente.idade), str(cliente.profissao))
    cursor.execute(sql_2, val)

def Excluir(id):
    cursor = db.db_connection.cursor()
    sql= "DELETE FROM projeto_trader.Cliente WHERE id = {}".format(id)
    cursor.execute(sql)
    db.db_connection.commit()

#Função serve para regastar os dados do BD

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM projeto_trader.Cliente")
    costmerList = []

    for row in db.cursor.fetchall(): # fetchal recupera todos os IDS selecionado acima
        costmerList.append(cliente.Cliente(row[0],row[1],row[2],row[3]))

    return costmerList




    # UPDATE `projeto_trader`.`Cliente` SET `cliNome` = 'Dagilla Almeida hjgh', `cliIdade` = '3132', `cliProfissao` = 'desenv23olvedor' WHERE (`id` = '19');
