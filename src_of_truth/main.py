# import inspect
import fire
from src_of_truth.commands import CommandExecutor

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
# http://localhost:7474/browser/


if __name__ == "__main__":
    fire.Fire(CommandExecutor(None))
