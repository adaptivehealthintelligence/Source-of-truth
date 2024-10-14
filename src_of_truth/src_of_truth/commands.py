from src_of_truth.neo4j import Neo4jConnection, get_connection
from typing import Optional
from src_of_truth.excel_utils import import_excel, df_to_cypher
import inspect
from .excel_utils import import_excel


class CommandExecutor:

    # region private
    def __init__(self, connection: Optional[Neo4jConnection]):
        self.__connection = connection if connection else get_connection()

    def __get_cmds(self, cmd_name=""):
        l = inspect.getmembers(self, predicate=inspect.ismethod)
        return [x for x in l if not x[0].startswith("_") and x[0].find(cmd_name) != -1]

    def __run_query(self, qry):
        return self.__connection.query(qry)

    def __run_command(self):
        cmds = self.__get_cmds(self.command)
        numcmds = len(cmds)
        if numcmds == 0:
            raise ValueError(f"Command {self.command} not found!")
        if numcmds > 1:
            raise ValueError(f"Command {self.command} has multiple matches!")
        return cmds[0][1]()

    def __print_results(self, nodes):
        if nodes is not None:
            for node in nodes:
                print(node)

    # endregion private

    def test_con(self):
        """Test the databse connection."""
        print("Testing neo4j connection.")
        self.__connection.verify_connectivity()
        print("Testing neo4j connection - succeeded!")

    def test_create(self):
        """Test the creation of a test record."""
        self.__run_query(
            'CREATE (test1:Test {name: "test 1", description: "first test"})'
        )

    def get_labels(self):
        """Get all labels."""
        qry = "MATCH (n) RETURN distinct labels(n)"
        nodes = self.__run_query(qry)
        self.__print_results(nodes)

    def get_all(self):
        """Get everything in the database."""
        qry = "MATCH (n) RETURN n"
        nodes = self.__run_query(qry)
        self.__print_results(nodes)

    def del_all(self):
        """Delete everything in the database."""
        self.__run_query("MATCH (n) DETACH DELETE n")

    def exe_file(self, filename: str):
        """Execute the commands in the <file> specified."""
        qry_str = None
        with open(filename, "r") as file:
            qry_str = file.read()
        print(f"Run query file={filename}")
        nodes = self.__run_query(qry_str)
        self.__print_results(nodes)

    def exe_str(self, query: str):
        """Execute the query in the 2nd parameter."""
        print(f"Run {query=}")
        nodes = self.__run_query(query)
        self.__print_results(nodes)

    def get_with_label(self, label: str):
        """Get all nodes for a <label>, like a table."""
        nodes = self.__run_query(f"match (n) where n:{label} return n;")
        self.__print_results(nodes)

    def load_excel(self, excel_fn: str):
        """Load the data from an excel sheet."""
        print(f"Loading data from {excel_fn}")
        df = import_excel(excel_fn)
        cypher_str = df_to_cypher(df, "Person", id_field="ID")
        nodes = self.__run_query(cypher_str)
        self.__print_results(nodes)

    def help_dep(self, command: str = ""):
        """Get the description for the <command>."""

        def display_help(cmd):
            print(f"{cmd[0]}:\t{cmd[1].__doc__}")

        for cmd in self.__get_cmds(command):
            display_help(cmd)


def run_command(connection: Neo4jConnection, command: str, *args):
    """Run the <command> with the <args>."""
    try:
        print(f"comands - Running command {command} with args {args}")
        cmd_exe = CommandExecutor(connection, command, *args)
    except Exception as e:
        print(f"Error running command {command}: {e}")
        return None
    return cmd_exe.result
