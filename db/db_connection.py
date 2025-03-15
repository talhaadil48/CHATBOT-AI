import pymysql
from pymysql.cursors import DictCursor
from config import DATABASE_CONFIG

class DBConnection:
    """
    Manages a single global DB connection using PyMySQL with DictCursor.
    """
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None or not cls._connection.open:
            try:
                cls._connection = pymysql.connect(
                    host=DATABASE_CONFIG["host"],
                    database=DATABASE_CONFIG["database"],
                    user=DATABASE_CONFIG["user"],
                    password=DATABASE_CONFIG["password"],
                    cursorclass=DictCursor
            )
                print("Database connected.")
            except pymysql.MySQLError as e:
                print("Error connecting to database:", e)
                raise e
        return cls._connection

    @classmethod
    def get_cursor(cls):
        return cls.get_connection().cursor()

    @classmethod
    def close_connection(cls):
        if cls._connection and cls._connection.open:
            cls._connection.close()
            print("Database connection closed.")
            cls._connection = None