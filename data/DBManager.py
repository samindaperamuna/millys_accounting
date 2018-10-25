import logging

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from util.StringUtil import StringUtil

Base = declarative_base()


class DBManager(object):
    _instance = None
    _engine = None
    _dbUrl = "postgresql://postgres:123@localhost"

    Session = None

    def __new__(cls):
        if DBManager._instance is None:
            DBManager._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self._engine = sqlalchemy.create_engine(self._dbUrl)

    def create_database(self, db_name, db_usr, db_pwd):
        # Generate Postgres safe identifiers.
        safe_db_name = StringUtil.pg_safe(db_name)
        safe_db_usr = StringUtil.pg_safe(db_usr)

        conn = self._engine.connect()

        # commit the current transaction so we can get a plain connection.
        # SQL DDL does not work within a transaction.
        conn.execute("COMMIT")

        db_created = False
        user_created = False
        user_assigned = False
        try:
            # Create the database.
            conn.execute("CREATE DATABASE {0}".format(safe_db_name))
            db_created = True
            conn.execute("CREATE USER {0} WITH ENCRYPTED PASSWORD '{1}'".format(safe_db_usr, db_pwd))
            user_created = True
            conn.execute("GRANT ALL PRIVILEGES ON DATABASE {0} TO {1}".format(safe_db_name, safe_db_usr))
            user_assigned = True

            # Initialise the database session attribute..
            engine = sqlalchemy.create_engine(
                "postgresql://{0}:{1}@localhost/{2}".format(safe_db_usr, db_pwd, safe_db_name))

            # Generate tables.
            Base.metadata.create_all(engine)

            # Generate session class.
            self.Session = sessionmaker(engine)
            return True
        except Exception as e:
            logging.error("Couldn't create database: {0}".format(str(e)))
        finally:
            conn.execute("COMMIT")

            try:
                if db_created and not user_created:
                    # If user is not assigned after database assignment, drop the database.
                    conn.execute("DROP DATABASE {0}".format(safe_db_name))
                elif user_created and not user_assigned:
                    # If unable to assign user drop user and the database.
                    conn.execute("DROP DATABASE {0}".format(safe_db_name))
                    conn.execute("DROP USER {0}".format(safe_db_usr))
            except Exception as e:
                logging.error("Couldn't rollback database creation: {0}".format(str(e)))
            finally:
                conn.close()

        return False
