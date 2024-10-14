from neo4j import GraphDatabase
from typing import Optional


class Neo4jConnection:
    """Neo4j connection class.

    This class is a wrapper around the neo4j driver. It is used to
    initialize the driver and to execute queries.

    Attributes:
        __uri (str): The URI of the neo4j database.
        __user (str): The user name for the neo4j database.
        __pwd (str): The password for the neo4j database.
        __driver (neo4j.driver): The neo4j driver.

    Usage:
        conn = Neo4jConnection(uri="bolt://52.87.123.11:7687", user="neo4j", pwd="hidden")

    """

    def __init__(
        self,
        uri,
        user,
        pwd,
        *,
        database: Optional[str] = None,
        home_dir: Optional[str] = None
    ):
        self.__uri: str = uri
        self.__user: str = user
        self.__pwd: str = pwd
        self.__database: str = database
        self.__home_dir: str = home_dir
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(
                self.__uri, auth=(self.__user, self.__pwd)
            )
        except Exception as e:
            print("Failed to create the driver:", e)

    def __del__(self):
        self.close()

    @property
    def home_dir(self):
        return self.__home_dir

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, parameters=None, database: Optional[str] = None):
        assert self.__driver is not None, "Driver not initialized!"
        db_arg = database if database is not None else self.__database
        # session = None
        # response = None
        try:
            session = (
                self.__driver.session(database=db_arg)
                if db_arg is not None
                else self.__driver.session()
            )
            response = list(session.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
            raise e
        finally:
            if session is not None:
                session.close()
        return response

    def verify_connectivity(self) -> None:
        self.__driver.verify_connectivity()


def get_connection():
    # for now the connection is hard coded here
    URI = "bolt://localhost:7687"  # "neo4j://localhost:7474"
    AUTH = ("neo4j", "Blah1234!")  #
    database = "test-load"
    neo4j_home = "/Users/tcoo5239/Library/Application Support/Neo4j Desktop/Application/relate-data/dbmss/dbms-7e2ec58e-7220-4352-9df2-c55e056a8288"
    return Neo4jConnection(
        URI, AUTH[0], AUTH[1], database=database, home_dir=neo4j_home
    )
