import pyodbc

class db:

    def __init__(self, banco, host, user, pwd ):
        self.__host = host
        self.__cursor =''
        self.__user = user
        self.__pwd = pwd
        if type == 'SQLSERVER':
            self.__Driver = "SQL Server"
        else:
            if type == 'MySQL':
                self.__Driver = "MySQL"


    def Conectar(self):
        Conexao = pyodbc.connect(DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=user;PWD=password)


