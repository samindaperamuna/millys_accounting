import sqlalchemy


class DBManager(object):
    _instance = None
    engine = None

    _dbUrl = "postgresql://postgres:123@localhost"

    def __new__(cls):
        if DBManager._instance is None:
            DBManager._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.engine = sqlalchemy.create_engine(self._dbUrl)

    def create_database(self, db_name, db_usr, db_pwd):
        conn = self.engine.connect()

        # commit the current transaction so we can get a plain connection.
        # SQL DDL does not work within a transaction.
        conn.execute("COMMIT")

        # Create the database.
        try:
            conn.execute("CREATE DATABASE {0}".format(db_name))
            conn.execute("CREATE USER {0} WITH ENCRYPTED PASSWORD '{1}'".format(db_usr, db_pwd))
            conn.execute("GRANT ALL PRIVILEGES ON DATABASE {0} TO {1}".format(db_name, db_usr))
        except Exception as e:
            print(e)
        finally:
            conn.close()
