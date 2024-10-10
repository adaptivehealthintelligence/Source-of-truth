from neo4j import GraphDatabase

# import inspect
import sys
from src_of_truth.neo4j_connection import Neo4jConnection
from src_of_truth.commands import run_command

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
# http://localhost:7474/browser/


# region old

_CMD_PREFIX = "cmd_"


def _get_cmd_funct_name(cmd_name):
    return _CMD_PREFIX + cmd_name


def _get_driver():
    URI = "neo4j://localhost"
    AUTH = ("neo4j", "Blah1234!")
    return GraphDatabase.driver(URI, auth=AUTH)


def cmd_test_con():
    """Test the databse connection."""
    with _get_driver() as driver:
        print("Testing neo4j connection.")
        driver.verify_connectivity()
        print("Testing neo4j connection - succeeded!")


def test_create():
    """Test the creation of a test record."""
    with _get_driver() as driver:
        session = driver.session()
        session.run('CREATE (test1:Test {name: "test 1", description: "first test"})')


def cmd_get_labels():
    """Get all labels."""
    with _get_driver() as driver:
        session = driver.session()
        qry = "MATCH (n) RETURN distinct labels(n)"
        nodes = session.run(qry)
        for node in nodes:
            print(node)


def cmd_get_all():
    """Get everything in the database."""
    with _get_driver() as driver:
        session = driver.session()
        qry = "MATCH (n) RETURN n"
        nodes = session.run(qry)
        for node in nodes:
            print(node)


def cmd_del_all():
    """Delete everything in the database."""
    with _get_driver() as driver:
        session = driver.session()
        session.run("MATCH (n) DETACH DELETE n")


def cmd_exe_file():
    """Execute the commands in the <file> specified."""
    fn = sys.argv[2]
    qry_str = None
    with open(fn, "r") as file:
        qry_str = file.read()
    print(f"Run query file={fn}")
    # print(f"{qry_str}")
    with _get_driver() as driver:
        session = driver.session()
        nodes = session.run(qry_str)
        for node in nodes:
            print(node)


def cmd_get_nodes_with_label():
    """Get all nodes for a <label>, like a table."""
    label = sys.argv[2]
    with _get_driver() as driver:
        session = driver.session()
        nodes = session.run(f"match (n) where n:{label} return n;")
        for node in nodes:
            print(node)


def cmd_help():
    """Get the description for the <command>."""

    def display_help(cmd_funct_name):
        cmd_name = cmd_funct_name[len(_CMD_PREFIX) :]
        print(f"{cmd_name}:\t{globals()[cmd_funct_name].__doc__}")

    if len(sys.argv) >= 3:
        cmd_name = sys.argv[2]
        cmd_funct_name = _get_cmd_funct_name(cmd_name)
        try:
            display_help(cmd_funct_name)
        except KeyError:
            print(f"Cannot find help for the command {cmd_name}.")
    else:
        print("list all commands:")
        for cmd in globals():
            if cmd.startswith(_CMD_PREFIX):
                display_help(cmd)


# endregion old


def get_sys_arg(index, default=None):
    try:
        return sys.argv[index]
    except IndexError:
        return default


def get_connection():
    # for now the connection is hard coded here
    URI = "bolt://localhost:7687"  # "neo4j://localhost:7474"
    AUTH = ("neo4j", "Blah1234!")  #
    database = "test-load"
    neo4j_home = "/Users/tcoo5239/Library/Application Support/Neo4j Desktop/Application/relate-data/dbmss/dbms-7e2ec58e-7220-4352-9df2-c55e056a8288"
    return Neo4jConnection(
        URI, AUTH[0], AUTH[1], database=database, home_dir=neo4j_home
    )


if __name__ == "__main__":
    run_command(get_connection(), get_sys_arg(1), *sys.argv[2:])
