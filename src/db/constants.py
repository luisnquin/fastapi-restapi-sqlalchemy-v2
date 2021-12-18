from os import getenv

DIALECT = "postgresql"
NAME = getenv("dbname")
USER = getenv("dbuser")
PASSWORD = getenv("dbpassword")
HOST = getenv("dbhost")
PORT = getenv("dbport")