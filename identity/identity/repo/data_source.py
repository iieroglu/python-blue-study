import mysql.connector.pooling
from mysql.connector import Error


class BaseDataSource:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def connect(self):
        raise NotImplemented

    def get_connection(self):
        raise NotImplemented


class MysqlDataSource(BaseDataSource):
    _cnx_pool = None

    def connect(self):
        try:
            config = {
                'user': self.kwargs.pop('db_user'),
                'password': self.kwargs.pop('db_pass'),
                'host': 'localhost',
                'port': '3306',
                'database': self.kwargs.pop('db_schema'),
                'raise_on_warnings': True
            }
            self._cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)
        except Error as e:
            print(e)

    def get_connection(self):
        return self._cnx_pool.get_connection()
